"""报告生成器
Author: harry666666
"""

from typing import Dict, List
from datetime import datetime
from pathlib import Path
from loguru import logger

class ReportGenerator:
    """HTML测试报告生成器"""
    
    def __init__(self, output_dir: str = "reports"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
    
    def generate_html_report(self, test_results: Dict) -> str:
        """生成HTML报告"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"report_{timestamp}.html"
        filepath = self.output_dir / filename
        
        html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>鲁棒性测试报告</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        h1 {{ color: #333; }}
        .summary {{ background: #f0f0f0; padding: 15px; border-radius: 5px; }}
        .pass {{ color: green; }}
        .fail {{ color: red; }}
        table {{ border-collapse: collapse; width: 100%; margin-top: 20px; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background-color: #4CAF50; color: white; }}
    </style>
</head>
<body>
    <h1>🚀 鲁棒性测试报告</h1>
    <div class="summary">
        <h2>测试概要</h2>
        <p>执行时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        <p>总用例数: {test_results.get('total', 0)}</p>
        <p class="pass">通过: {test_results.get('passed', 0)}</p>
        <p class="fail">失败: {test_results.get('failed', 0)}</p>
        <p>通过率: {test_results.get('pass_rate', 0):.2f}%</p>
    </div>
    
    <h2>详细结果</h2>
    <table>
        <tr>
            <th>测试用例</th>
            <th>状态</th>
            <th>耗时(ms)</th>
            <th>备注</th>
        </tr>
        {''.join(self._generate_row(r) for r in test_results.get('details', []))}
    </table>
</body>
</html>
"""
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        logger.info(f"报告已生成: {filepath}")
        return str(filepath)
    
    def _generate_row(self, result: Dict) -> str:
        """生成表格行"""
        status_class = 'pass' if result.get('passed') else 'fail'
        status_text = '✓ 通过' if result.get('passed') else '✗ 失败'
        
        return f"""
        <tr>
            <td>{{result.get('name', 'N/A')}}</td>
            <td class="{{status_class}}">{{status_text}}</td>
            <td>{{result.get('duration', 0):.2f}}</td>
            <td>{{result.get('note', '')}}</td>
        </tr>
        """