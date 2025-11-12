# 贡献指南

感谢你对 Robustness Test Framework 的关注！我们欢迎所有形式的贡献。

## 如何贡献

### 报告问题

如果你发现了 bug 或有功能建议：

1. 在 [Issues](https://github.com/harry666666/robustness-test-framework/issues) 中搜索是否已有相关问题
2. 如果没有，创建一个新的 Issue
3. 清楚地描述问题或建议
4. 如果是 bug，提供复现步骤

### 提交代码

1. **Fork 仓库**
   ```bash
   # Fork 后克隆到本地
   git clone https://github.com/YOUR_USERNAME/robustness-test-framework.git
   cd robustness-test-framework
   ```

2. **创建分支**
   ```bash
   git checkout -b feature/your-feature-name
   # 或
   git checkout -b fix/your-bug-fix
   ```

3. **编写代码**
   - 遵循现有的代码风格
   - 添加必要的测试
   - 更新相关文档

4. **运行测试**
   ```bash
   pytest tests/ -v
   ```

5. **提交更改**
   ```bash
   git add .
   git commit -m "feat: 添加新功能"
   # 或
   git commit -m "fix: 修复某个问题"
   ```

6. **推送到 GitHub**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **创建 Pull Request**
   - 在 GitHub 上创建 PR
   - 描述你的更改
   - 链接相关的 Issue

## 提交信息规范

我们使用 [Conventional Commits](https://www.conventionalcommits.org/) 规范：

- `feat:` 新功能
- `fix:` Bug 修复
- `docs:` 文档更新
- `style:` 代码格式调整
- `refactor:` 重构
- `test:` 测试相关
- `chore:` 构建/工具链相关

示例：
```
feat: 添加网络超时重试机制
fix: 修复并发测试中的死锁问题
docs: 更新 README 中的安装说明
```

## 代码风格

- 使用 Python 3.9+ 特性
- 遵循 PEP 8 规范
- 使用 type hints
- 编写清晰的注释和文档字符串

### 代码格式化

推荐使用以下工具：

```bash
# 格式化代码
black .

# 检查代码风格
flake8 .

# 类型检查
mypy .
```

## 测试指南

### 编写测试

- 为新功能编写单元测试
- 确保测试覆盖率不降低
- 测试应该快速且可靠

### 运行测试

```bash
# 运行所有测试
pytest tests/ -v

# 运行特定测试
pytest tests/test_abnormal_input.py -v

# 查看覆盖率
pytest tests/ --cov=. --cov-report=html
```

## 文档

- 更新 README.md（如果需要）
- 更新 CHANGELOG.md
- 为新功能添加使用示例
- 更新 API 文档

## Pull Request 检查清单

提交 PR 前，请确保：

- [ ] 代码遵循项目风格
- [ ] 所有测试通过
- [ ] 添加了必要的测试
- [ ] 更新了相关文档
- [ ] commit 信息符合规范
- [ ] PR 描述清晰

## 获取帮助

如果有任何问题：

- 查看 [文档](https://github.com/harry666666/robustness-test-framework)
- 在 [Issues](https://github.com/harry666666/robustness-test-framework/issues) 中提问
- 联系维护者

## 行为准则

- 尊重他人
- 接受建设性批评
- 关注对项目最有利的事情
- 对社区其他成员表示同理心

感谢你的贡献！🎉