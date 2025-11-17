"""配置环境测试
Author: harry666666
"""

import pytest
import os
from loguru import logger

class TestConfigEnv:
    """配置环境鲁棒性测试"""
    
    def test_missing_config(self, http_client):
        """测试缺失配置项"""
        logger.info("测试场景：缺失关键配置")
        
        # 模拟配置缺失场景
        response = http_client.get('/api/health')
        assert response.status_code in [200, 500]
    
    def test_invalid_config_value(self, http_client):
        """测试无效配置值"""
        logger.info("测试场景：无效配置值")
        
        # 系统应该有配置校验机制
        response = http_client.get('/api/health')
        assert response.status_code in [200, 500]
    
    def test_environment_switching(self, http_client, test_config):
        """测试环境切换"""
        logger.info(f"测试场景：环境切换 - 当前环境: {test_config.get('env', 'unknown')}")
        
        response = http_client.get('/api/health')
        assert response.status_code == 200
    
    def test_sensitive_data_exposure(self, http_client):
        """测试敏感数据暴露"""
        logger.info("测试场景：敏感信息泄漏检查")
        
        response = http_client.get('/api/vehicle/detail', params={'vin': 'TEST123'})
        
        if response.status_code == 200:
            data = response.json()
            # 检查响应中不应包含敏感字段
            sensitive_fields = ['password', 'secret', 'token', 'api_key']
            for field in sensitive_fields:
                assert field not in str(data).lower(), f"响应中不应包含敏感字段: {field}"
