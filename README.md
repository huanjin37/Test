# 🚀 Web UI自动化测试框架

基于POM（页面对象模型）设计模式的Web自动化测试框架，使用Python + Selenium + Pytest + Allure构建。

## ✨ 特性

- ✅ **POM设计模式**：页面元素与测试逻辑分离，提高代码可维护性
- ✅ **智能等待机制**：告别硬性等待，提升测试执行效率
- ✅ **数据驱动测试**：支持JSON/YAML测试数据管理
- ✅ **Allure报告**：生成美观的自动化测试报告
- ✅ **多浏览器支持**：支持Chrome、Edge等主流浏览器
- ✅ **持续集成就绪**：已配置GitHub Actions工作流

## 🛠️ 技术栈

- **语言**：Python 3.8+
- **测试框架**：Pytest
- **浏览器自动化**：Selenium WebDriver
- **报告工具**：Allure-pytest
- **页面对象模型**：POM设计模式
- **持续集成**：GitHub Actions

## 📁 项目结构
web_auto_test/
├── pages/ # 页面对象层
│ ├── base_page.py # 基础页面类（封装通用方法）
│ └── baidu_page.py # 百度页面类
├── tests/ # 测试用例层
│ ├── test_baidu_pom.py # 百度搜索测试（POM模式）
│ └── test_baidu_search.py # 基础测试用例
├── test_data/ # 测试数据文件
├── reports/ # 测试报告输出
├── screenshots/ # 失败截图
├── .github/workflows/ # CI/CD配置
├── .gitignore
├── README.md
├── requirements.txt
├── conftest.py
└── pytest.ini
## 🚀 快速开始

### 1. 环境准备
```bash
# 克隆项目
git clone git@github.com:huanjin37/Test.git
cd web_auto_test

# 安装依赖
pip install -r requirements.txt



<img width="2546" height="1401" alt="image" src="https://github.com/user-attachments/assets/e6ec15e9-9a49-40bc-880b-74f73484c0ca" />
<img width="2537" height="1412" alt="image (3)" src="https://github.com/user-attachments/assets/a21a96b7-c42d-4e5f-9bda-d575642e1f97" />
<img width="2559" height="1461" alt="image (2)" src="https://github.com/user-attachments/assets/cf213bd3-2cc9-49fc-8816-3b419f5da812" />
<img width="2545" height="1400" alt="image (1)" src="https://github.com/user-attachments/assets/e793b9c3-c4f6-4065-a176-be2332caa916" />
