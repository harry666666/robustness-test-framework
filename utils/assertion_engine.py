"""断言引擎
Author: harry666666
"""

import yaml
from typing import Dict, Any, List
from loguru import logger
import requests

class AssertionEngine:
    """智能断言引擎"""
    
    def __init__(self, config_path: str = "config/assertion_rules.yaml"):
        with open(config_path) as f:
            self.rules = yaml.safe_load(f)
    
    def assert_response_time(self, response: requests.Response, max_time_ms: int = None):
        """断言响应时间"""
        elapsed_ms = response.elapsed.total_seconds() * 1000
        max_time = max_time_ms or self.rules['rules']['response_time']['normal']
        
        assert elapsed_ms < max_time, f"响应时间过长: {elapsed_ms:.2f}ms > {max_time}ms"
        logger.info(f"✓ 响应时间正常: {elapsed_ms:.2f}ms")
    
    def assert_status_code(self, response: requests.Response, expected_codes: List[int] = None):
        """断言状态码"""
        expected = expected_codes or self.rules['rules']['status_codes']['success']
        
        assert response.status_code in expected, \
            f"状态码异常: {response.status_code} not in {expected}"
        logger.info(f"✓ 状态码正常: {response.status_code}")
    
    def assert_json_schema(self, response: requests.Response, required_fields: List[str]):
        """断言JSON结构"""
        try:
            data = response.json()
        except:
            raise AssertionError("响应不是有效的JSON")
        
        for field in required_fields:
            assert field in data, f"缺少必需字段: {field}"
        
        logger.info(f"✓ JSON结构正常，包含所有必需字段: {required_fields}")
    
    def assert_headers(self, response: requests.Response):
        """断言响应头"""
        required_headers = self.rules['rules'].get('required_headers', [])
        
        for header in required_headers:
            assert header in response.headers, f"缺少必需的响应头: {header}"
        
        logger.info(f"✓ 响应头完整")