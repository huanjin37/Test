from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class BaiduPage(BasePage):
    SEARCH_INPUT=(By.ID,"chat-textarea")
    SEARCH_BUTTON=(By.ID,"chat-submit-button")
    SEARCH_RESULTS=(By.ID,"content_left")

    def open_baidu(self):
        self.driver.get("https://www.baidu.com")
        #self.take_screenshot("打开百度首页")
        return self 
    
    def search(self,keyword):
        self.input_text(*self.SEARCH_INPUT,keyword)
        self.click(*self.SEARCH_BUTTON)
        """
        import time
        time.sleep(2)
        """
        self.wait_for_title_contains("百度搜索")
        print(f"搜索成功！当前标题: {self.driver.title}")
        return self 
    
    def get_search_results_text(self):
        retur=self.find_element(*self.SEARCH_RESULTS)
        return results.text
    """
    def search(self, keyword):
        
        print(f"开始搜索: {keyword}")
    
    # 1. 找到搜索框并输入
        search_input = self.find_element(*self.SEARCH_INPUT)
        print(f"找到搜索框: {search_input}")
        search_input.clear()
        search_input.send_keys(keyword)
        print(f"已输入关键词: {keyword}")
    
    # 2. 找到搜索按钮并点击
        search_button = self.find_element(*self.SEARCH_BUTTON)
        print(f"找到搜索按钮: {search_button}")
        search_button.click()
        print("已点击搜索按钮")
    
    # 3. 等待页面跳转（重要！）
        import time
        time.sleep(2)  # 简单等待2秒，稍后我们会用更智能的方法
    
    # 4. 打印当前URL和标题，看看是否跳转成功
        print(f"当前URL: {self.driver.current_url}")
        print(f"当前标题: {self.driver.title}")
    
        return self
    """    
    def get_title(self):
        title = self.driver.title
        print(f"获取到的标题: {title}")
        return title