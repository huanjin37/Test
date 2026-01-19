from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class BasePage:

    def __init__(self,driver):
        self.driver =driver
        self.wait =WebDriverWait(driver,10)

    def find_element (self,by,locator):
        try:
            return self.wait.until(EC.presence_of_element_located((by,locator)))
        except Exception as e:
            self.take_screenshot("查找元素失败")
            raise Exception(f"找不到元素：{locator},错误：{str(e)}")

    def click(self,by,locator):
        element =self.find_element(by,locator)
        element.click()

    def input_text(self,by,locator,text):
        element =self.find_element(by,locator)
        element.clear()
        element.send_keys(text)       
    
    def get_title(self):
        return self.driver.title

    def wait_for_title_contains(self, text, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.title_contains(text)
            )
        except:
            print(f"等待失败：期望标题包含'{text}'，实际标题为'{self.driver.title}'")
        return False
            
    
    def wait_for_url_contains(self, text, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.url_contains(text)
            )
            return True
        except:
            return False
           