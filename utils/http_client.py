"""HTTP客户端工具
Author: harry666666
"""

import requests
from typing import Dict, Optional, Any
from loguru import logger
from tenacity import retry, stop_after_attempt, wait_exponential

class RobustnessHttpClient:
    """增强型HTTP客户端，支持超时、重试、日志"""
    
    def __init__(self, base_url: str, default_timeout: int = 5):
        self.base_url = base_url.rstrip('/')
        self.default_timeout = default_timeout
        self.session = requests.Session()
        
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=1, max=10)
    )
    def get(self, endpoint: str, **kwargs) -> requests.Response:
        """GET请求"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        kwargs.setdefault('timeout', self.default_timeout)
        
        logger.info(f"[GET] {url}")
        response = self.session.get(url, **kwargs)
        logger.info(f"[RESPONSE] {response.status_code} - {response.elapsed.total_seconds():.3f}s")
        
        return response
    
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=1, max=10)
    )
    def post(self, endpoint: str, json: Optional[Dict] = None, **kwargs) -> requests.Response:
        """POST请求"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        kwargs.setdefault('timeout', self.default_timeout)
        
        logger.info(f"[POST] {url} | Body: {json}")
        response = self.session.post(url, json=json, **kwargs)
        logger.info(f"[RESPONSE] {response.status_code} - {response.elapsed.total_seconds():.3f}s")
        
        return response
    
    def put(self, endpoint: str, json: Optional[Dict] = None, **kwargs) -> requests.Response:
        """PUT请求"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        kwargs.setdefault('timeout', self.default_timeout)
        
        logger.info(f"[PUT] {url} | Body: {json}")
        response = self.session.put(url, json=json, **kwargs)
        logger.info(f"[RESPONSE] {response.status_code}")
        
        return response
    
    def delete(self, endpoint: str, **kwargs) -> requests.Response:
        """DELETE请求"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        kwargs.setdefault('timeout', self.default_timeout)
        
        logger.info(f"[DELETE] {url}")
        response = self.session.delete(url, **kwargs)
        logger.info(f"[RESPONSE] {response.status_code}")
        
        return response