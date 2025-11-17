"""数据生成器
Author: harry666666
"""

from faker import Faker
import random
import string
from typing import List, Any

fake = Faker('zh_CN')

class DataGenerator:
    """测试数据生成器"""
    
    @staticmethod
    def random_string(length: int = 10) -> str:
        """生成随机字符串"""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    
    @staticmethod
    def random_email() -> str:
        """生成随机邮箱"""
        return fake.email()
    
    @staticmethod
    def random_phone() -> str:
        """生成随机手机号"""
        return fake.phone_number()
    
    @staticmethod
    def random_vin() -> str:
        """生成随机VIN码（17位）"""
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=17))
    
    @staticmethod
    def sql_injection_payloads() -> List[str]:
        """SQL注入payload"""
        return [
            "' OR 1=1; --",
            "'; DROP TABLE users; --",
            "' UNION SELECT NULL, NULL, NULL--",
            "admin'--",
            "' OR 'a'='a"
        ]
    
    @staticmethod
    def xss_payloads() -> List[str]:
        """XSS攻击payload"""
        return [
            "<script>alert('xss')</script>",
            "<img src=x onerror=alert('xss')>",
            "<svg onload=alert('xss')>",
            "javascript:alert('xss')"
        ]
    
    @staticmethod
    def boundary_values(field_type: str) -> List[Any]:
        """边界值测试数据"""
        boundaries = {
            'int': [-2147483648, -1, 0, 1, 2147483647],
            'string': ['', 'a', 'a' * 255, 'a' * 1000],
            'array': [[], [1], list(range(1000))]
        }
        return boundaries.get(field_type, [])