"""
Pytest全局配置
Author: harry666666
"""

import pytest
import yaml
from pathlib import Path

def pytest_addoption(parser):
    """添加自定义命令行选项"""
    parser.addoption(
        "--config",
        action="store",
        default="config/test_config.yaml",
        help="配置文件路径"
    )
    
    parser.addoption(
        "--with-chaos",
        action="store_true",
        default=False,
        help="启用混沌工程测试"
    )
    
    parser.addoption(
        "--base-url",
        action="store",
        default=None,
        help="覆盖配置文件中的base_url"
    )

@pytest.fixture(scope="session")
def test_config(request):
    """加载测试配置"""
    config_path = request.config.getoption("--config")
    
    with open(config_path) as f:
        config = yaml.safe_load(f)
    
    # 命令行参数覆盖
    base_url = request.config.getoption("--base-url")
    if base_url:
        config['api']['base_url'] = base_url
    
    return config

@pytest.fixture(scope="session")
def http_client(test_config):
    """HTTP客户端fixture"""
    from utils.http_client import RobustnessHttpClient
    
    client = RobustnessHttpClient(
        base_url=test_config['api']['base_url'],
        default_timeout=test_config['api'].get('timeout', 5)
    )
    yield client
    client.session.close()

@pytest.fixture
def enable_chaos(request):
    """混沌工程开关"""
    return request.config.getoption("--with-chaos")
