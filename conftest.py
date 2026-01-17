import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    print("\n正在启动Edge浏览器")
    driver_instance = webdriver.Edge()
    driver_instance.implicitly_wait(5)

    yield driver_instance

    print("\n正在退出Edge浏览器")
    driver_instance.quit()