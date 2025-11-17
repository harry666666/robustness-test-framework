"""输入异常测试
Author: harry666666
"""

import pytest
from utils.data_generator import DataGenerator
from loguru import logger

class TestInputAnomaly:
    """输入异常鲁棒性测试"""
    
    def test_null_input(self, http_client, test_config):
        """测试空值输入"""
        logger.info("测试场景：空值输入")
        response = http_client.post('/api/identify', json={'vin': None})
        assert response.status_code in [400, 422], "应该拒绝空值输入"
    
    def test_empty_string(self, http_client):
        """测试空字符串"""
        logger.info("测试场景：空字符串")
        response = http_client.post('/api/identify', json={'vin': ''})
        assert response.status_code == 400
    
    def test_oversized_string(self, http_client):
        """测试超长字符串"""
        logger.info("测试场景：超长字符串（10000字符）")
        oversized = DataGenerator.random_string(10000)
        response = http_client.post('/api/identify', json={'vin': oversized})
        assert response.status_code in [400, 413]
    
    def test_sql_injection(self, http_client):
        """测试SQL注入"""
        logger.info("测试场景：SQL注入攻击")
        for payload in DataGenerator.sql_injection_payloads():
            response = http_client.post('/api/identify', json={'vin': payload})
            assert response.status_code in [400, 403], f"应该拦截SQL注入: {payload}"
    
    def test_xss_attack(self, http_client):
        """测试XSS攻击"""
        logger.info("测试场景：XSS攻击")
        for payload in DataGenerator.xss_payloads():
            response = http_client.post('/api/identify', json={'vin': payload})
            assert response.status_code in [400, 403], f"应该拦截XSS: {payload}"
    
    def test_invalid_vin_format(self, http_client):
        """测试无效VIN格式"""
        logger.info("测试场景：无效VIN格式")
        invalid_vins = ['ABC', '12345', 'TOOLONG' * 10]
        for vin in invalid_vins:
            response = http_client.post('/api/identify', json={'vin': vin})
            assert response.status_code == 400
    
    @pytest.mark.parametrize('boundary', DataGenerator.boundary_values('int'))
    def test_integer_boundary(self, http_client, boundary):
        """测试整数边界值"""
        logger.info(f"测试场景：整数边界值 {boundary}")
        response = http_client.post('/api/transfer/create', json={'amount': boundary})
        assert response.status_code in [200, 201, 400]