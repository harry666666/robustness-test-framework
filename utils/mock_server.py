"""Mock服务器
Author: harry666666
"""

from flask import Flask, jsonify, request
import random
import time
from loguru import logger

app = Flask(__name__)

@app.route('/api/identify', methods=['POST'])
def identify():
    """车辆识别接口"""
    data = request.json
    vin = data.get('vin')
    
    # 模拟随机延迟
    time.sleep(random.uniform(0.1, 0.5))
    
    if not vin or len(vin) != 17:
        return jsonify({'error': 'Invalid VIN'}), 400
    
    return jsonify({
        'vin': vin,
        'brand': 'ZEEKR',
        'model': '001',
        'year': 2023
    }), 200

@app.route('/api/transfer/create', methods=['POST'])
def create_transfer():
    """创建过户记录"""
    data = request.json
    
    # 模拟10%的失败率
    if random.random() < 0.1:
        return jsonify({'error': 'Service temporarily unavailable'}), 503
    
    return jsonify({
        'transfer_id': f"T{random.randint(10000, 99999)}",
        'status': 'pending'
    }), 201

@app.route('/api/vehicle/detail', methods=['GET'])
def vehicle_detail():
    """车辆详情查询"""
    vin = request.args.get('vin')
    
    if not vin:
        return jsonify({'error': 'VIN required'}), 400
    
    return jsonify({
        'vin': vin,
        'owner': 'Test User',
        'mileage': 15000,
        'last_service': '2024-01-15'
    }), 200

@app.route('/health', methods=['GET'])
def health():
    """健康检查"""
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    logger.info("启动Mock服务器...")
    app.run(host='0.0.0.0', port=8080, debug=True)