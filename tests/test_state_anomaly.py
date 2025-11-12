"""状态异常测试
Author: harry666666
"""

import pytest
from loguru import logger
from utils.data_generator import DataGenerator

class TestStateAnomaly:
    """状态异常鲁棒性测试"""
    
    def test_idempotency(self, http_client):
        """测试幂等性"""
        logger.info("测试场景：幂等性检查")
        
        vin = DataGenerator.random_vin()
        payload = {'vin': vin, 'user_id': 'U123'}
        
        # 连续发送3次相同请求
        response1 = http_client.post('/api/transfer/create', json=payload)
        response2 = http_client.post('/api/transfer/create', json=payload)
        response3 = http_client.post('/api/transfer/create', json=payload)
        
        # 幂等性检查：多次请求应该返回相同结果或合理的409
        assert response1.status_code in [200, 201]
        assert response2.status_code in [200, 201, 409]
        assert response3.status_code in [200, 201, 409]
    
    def test_state_transition(self, http_client):
        """测试状态转换"""
        logger.info("测试场景：非法状态转换")
        
        vin = DataGenerator.random_vin()
        
        # 创建过户记录
        response = http_client.post('/api/transfer/create', json={
            'vin': vin,
            'user_id': 'U123'
        })
        
        if response.status_code in [200, 201]:
            transfer_id = response.json().get('transfer_id')
            
            # 尝试非法状态转换
            invalid_transition = http_client.put(f'/api/transfer/{transfer_id}', json={
                'status': 'invalid_status'
            })
            
            assert invalid_transition.status_code in [400, 422]
    
    def test_concurrent_state_update(self, http_client):
        """测试并发状态更新"""
        logger.info("测试场景：并发状态更新冲突")
        
        from concurrent.futures import ThreadPoolExecutor
        
        vin = DataGenerator.random_vin()
        
        def update_state(i):
            return http_client.post('/api/transfer/create', json={
                'vin': vin,
                'user_id': f'U{i}'
            })
        
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(update_state, i) for i in range(10)]
            responses = [f.result() for f in futures]
        
        # 应该有冲突检测机制
        status_codes = [r.status_code for r in responses]
        logger.info(f"状态码分布: {status_codes}")
