# Robustness Test Framework

一个用于AI服务鲁棒性测试的自动化测试框架。

## 功能特性

- ✅ 多维度鲁棒性测试
- ✅ 自动化测试执行
- ✅ 详细的测试报告生成
- ✅ Docker容器化支持
- ✅ CI/CD集成

## 测试类型

### 1. 异常输入测试
- 空值/null输入
- 超长文本
- 特殊字符
- 格式错误的数据

### 2. 边界条件测试
- 最小/最大值
- 临界点测试
- 边界值组合

### 3. 并发压力测试
- 高并发请求
- 资源竞争
- 死锁检测

### 4. 网络异常测试
- 超时处理
- 连接中断
- 重试机制

### 5. 数据一致性测试
- 事务完整性
- 数据验证
- 状态一致性

## 快速开始

### 环境要求
- Python 3.9+
- Docker & Docker Compose (可选)

### 安装依赖

```bash
pip install -r requirements.txt
```

### 运行测试

#### 1. 运行所有测试
```bash
python run_all_tests.py
```

#### 2. 运行特定类型测试
```bash
# 异常输入测试
pytest tests/test_abnormal_input.py -v

# 边界条件测试
pytest tests/test_boundary_condition.py -v

# 并发压力测试
pytest tests/test_concurrent_stress.py -v

# 网络异常测试
pytest tests/test_network_exception.py -v

# 数据一致性测试
pytest tests/test_data_consistency.py -v
```

#### 3. 使用Docker运行
```bash
docker-compose up --build
```

## 项目结构

```
robustness-test-framework/
├── tests/                      # 测试用例
│   ├── test_abnormal_input.py
│   ├── test_boundary_condition.py
│   ├── test_concurrent_stress.py
│   ├── test_network_exception.py
│   └── test_data_consistency.py
├── utils/                      # 工具类
│   ├── logger.py
│   ├── report_generator.py
│   └── mock_server.py
├── config/                     # 配置文件
│   └── test_config.yaml
├── reports/                    # 测试报告
├── logs/                       # 日志文件
├── .github/                    # CI/CD配置
│   └── workflows/
│       └── ci.yml
├── requirements.txt            # Python依赖
├── Dockerfile                  # Docker配置
├── docker-compose.yml          # Docker Compose配置
├── run_all_tests.py           # 测试运行器
└── README.md                   # 项目文档
```

## 测试报告

测试完成后，会在 `reports/` 目录生成以下报告：
- HTML报告: `test_report_YYYYMMDD_HHMMSS.html`
- JSON报告: `test_report_YYYYMMDD_HHMMSS.json`

## 日志

日志文件保存在 `logs/` 目录：
- `test_YYYYMMDD.log`: 每日测试日志

## CI/CD集成

本项目支持GitHub Actions自动化测试：
- 每次push或PR都会自动运行测试
- 测试报告和日志会自动上传为artifacts

## 贡献指南

1. Fork本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启Pull Request

## 许可证

MIT License

## 联系方式

- 作者: harry666666
- 项目链接: https://github.com/harry666666/robustness-test-framework