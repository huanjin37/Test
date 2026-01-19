import allure
import pytest
from pages.baidu_page import BaiduPage

@allure.epic("Web UI自动化测试项目")
@allure.feature("百度搜索测试 - POM模式")
class TestBaiduSearchPOM:

    @allure.story("基本搜索功能")
    @allure.title("测试百度搜索功能 - 搜索{keyword}")
    @pytest.mark.parametrize("keyword",["selenium","Python","自动化测试"])
    def test_search(self,driver,keyword):
        baidu_page=BaiduPage(driver)
        
        baidu_page.open_baidu().search(keyword)

        assert keyword in baidu_page.get_title()
        
        print(f"搜索 '{keyword}' 成功，标题: {baidu_page.get_title()}")

    @allure.story("页面元素验证")
    @allure.title("验证百度首页元素")
    def test_homepage_elements(self, driver):
        """验证百度首页元素"""
        baidu_page = BaiduPage(driver)
        baidu_page.open_baidu()
        
        search_input = baidu_page.find_element(*BaiduPage.SEARCH_INPUT)
        assert search_input.is_displayed()
        
        search_button = baidu_page.find_element(*BaiduPage.SEARCH_BUTTON)
        assert search_button.is_displayed()
        
        print("百度首页元素验证通过")