from setuptools import setup, find_packages

setup(
    name="robustness-test-framework",
    version="1.0.0",
    author="harry666666",
    description="通用鲁棒性测试框架 - 覆盖7大维度52个测试场景",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/harry666666/robustness-test-framework",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=open("requirements.txt").read().splitlines(),
)