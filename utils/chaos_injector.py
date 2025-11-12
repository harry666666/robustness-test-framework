"""
混沌注入器
Author: harry666666
"""

import time
import random
from typing import Callable, Any
from loguru import logger

class ChaosInjector:
    """混沌工程注入器"""
    
    @staticmethod
    def inject_latency(func: Callable, delay_ms: int) -> Any:
        """注入延迟"""
        logger.warning(f"[CHAOS] 注入延迟: {delay_ms}ms")
        time.sleep(delay_ms / 1000)
        return func()
    
    @staticmethod
    def inject_timeout(func: Callable, timeout: float = 0.1) -> Any:
        """注入超时（通过极短超时模拟）"""
        logger.warning(f"[CHAOS] 注入超时: {timeout}s")
        import signal
        
        def timeout_handler(signum, frame):
            raise TimeoutError("Chaos timeout injected")
        
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(int(timeout))
        
        try:
            result = func()
            signal.alarm(0)
            return result
        except TimeoutError:
            logger.error("超时异常被触发")
            raise
    
    @staticmethod
    def inject_random_failure(func: Callable, failure_rate: float = 0.3) -> Any:
        """随机注入失败"""
        if random.random() < failure_rate:
            logger.warning(f"[CHAOS] 注入随机失败 (概率: {failure_rate})")
            raise Exception("Chaos random failure injected")
        
        return func()
    
    @staticmethod
    def inject_partial_response(response_data: dict, drop_rate: float = 0.5) -> dict:
        """注入不完整响应"""
        logger.warning(f"[CHAOS] 注入不完整响应 (丢失率: {drop_rate})")
        
        keys = list(response_data.keys())
        drop_count = int(len(keys) * drop_rate)
        drop_keys = random.sample(keys, drop_count)
        
        return {k: v for k, v in response_data.items() if k not in drop_keys}