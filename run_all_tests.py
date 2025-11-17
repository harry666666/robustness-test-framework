#!/usr/bin/env python3
"""
鲁棒性测试统一执行入口
Author: harry666666
Date: 2025-01-12
"""

import sys
import argparse
import pytest
from pathlib import Path
from datetime import datetime
from loguru import logger

def parse_args():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(description='鲁棒性测试框架')
    
    parser.add_argument(
        '--config',
        default='config/test_config.yaml',
        help='配置文件路径（默认: config/test_config.yaml）'
    )
    
    parser.add_argument(
        '--dimension',
        choices=['input', 'protocol', 'dependency', 'concurrency', 'state', 'config', 'recovery', 'all'],
        default='all',
        help='测试维度（默认: all）'
    )
    
    parser.add_argument(
        '--markers',
        default='not load_test',
        help='Pytest标记过滤（默认: not load_test）'
    )
    
    parser.add_argument(
        '--parallel',
        type=int,
        default=1,
        help='并行执行进程数（默认: 1）'
    )
    
    parser.add_argument(
        '--output',
        default='reports',
        help='报告输出目录（默认: reports）'
    )
    
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='详细输出'
    )
    
    return parser.parse_args()

def get_test_path(dimension: str) -> str:
    """根据维度获取测试路径"""
    dimension_map = {
        'input': 'tests/test_input_anomaly.py',
        'protocol': 'tests/test_protocol_anomaly.py',
        'dependency': 'tests/test_dependency_fault.py',
        'concurrency': 'tests/test_concurrency.py',
        'state': 'tests/test_state_anomaly.py',
        'config': 'tests/test_config_env.py',
        'recovery': 'tests/test_recovery.py',
        'all': 'tests/'
    }
    return dimension_map.get(dimension, 'tests/')

def main():
    """主函数"""
    args = parse_args()
    
    # 配置日志
    log_file = f"reports/test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    logger.add(
        log_file,
        rotation="10 MB",
        retention="7 days",
        level="DEBUG" if args.verbose else "INFO"
    )
    
    logger.info("=" * 80)
    logger.info("鲁棒性测试开始执行")
    logger.info(f"配置文件: {args.config}")
    logger.info(f"测试维度: {args.dimension}")
    logger.info(f"执行时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info("=" * 80)
    
    # 创建报告目录
    output_path = Path(args.output)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # 构建pytest参数
    test_path = get_test_path(args.dimension)
    
    pytest_args = [
        test_path,
        "-v" if args.verbose else "-q",
        "-s",
        "--tb=short",
        f"--html={output_path}/robustness_report.html",
        "--self-contained-html",
        f"--junit-xml={output_path}/junit.xml",
        f"-m", args.markers,
        "--maxfail=20",
    ]
    
    # 并行执行
    if args.parallel > 1:
        pytest_args.extend(["-n", str(args.parallel)])
    
    logger.info(f"Pytest参数: {' '.join(pytest_args)}")
    
    # 执行测试
    exit_code = pytest.main(pytest_args)
    
    # 输出摘要
    logger.info("=" * 80)
    if exit_code == 0:
        logger.success("✅ 所有测试通过！")
    else:
        logger.error(f"❌ 测试失败，退出码: {exit_code}")
    logger.info(f"详细报告: {output_path}/robustness_report.html")
    logger.info("=" * 80)
    
    return exit_code

if __name__ == "__main__":
    sys.exit(main())