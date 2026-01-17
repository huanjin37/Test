#from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#显示等待
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#2
import allure

@allure.epic("Web UI自动化测试项目")
@allure.feature("百度核心业务")
@allure.story("搜索功能验证")
def test_baidu_search_basic(driver):
    """driver =webdriver.Edge()
    #隐式等待
    driver.implicitly_wait(5)
    """

    try:
        with allure.step("步骤1：导航到百度首页"):
            driver.get("https://baidu.com")
            allure.attach(driver.get_screenshot_as_png(),name='首页截图',attachment_type=allure.attachment_type.PNG)
            print("已打开百度")
            time.sleep(3)

        
        with allure.step("步骤2：导航到百度首页"):
            wait =WebDriverWait(driver,10)
            search_input =driver.find_element(By.ID,'chat-textarea')
            search_input.send_keys('Selenium自动化测试')
            print("已在搜索框中输入关键词")
            time.sleep(3)

        with allure.step("步骤3：点击百度一下按钮"):
            search_button =driver.find_element(By.ID,'chat-submit-button')
            search_button.click()
            print("已点击按钮")

            time.sleep(2)
 
        with allure.step("步骤4：验证搜索结果"):
            wait.until(EC.presence_of_all_elements_located((By.ID,"content_left"))) 
            allure.attach(driver.get_screenshot_as_png(),name='结果截图',attachment_type=allure.attachment_type.PNG)
            assert "Selenium" in driver.title
            print ("测试通过！页面包含Selenium。")
        """
        result_element =driver.find_element(By.PARTIAL_LINK_TEXT,"selenium")
        assert result_element is not None
        print("测试通过，找到包含selenium的链接")
        """

    except Exception as e:
        allure.attach(driver.get_screenshot_as_png(),name="异常截图",attachment_type=allure.attachment_type.PNG)
        """
        print(f"测试过程出错：{e}")
        assert False,f"测试失败，原因：{e}"
        """
        raise e

    finally:
        print("测试结束")
        #driver.quit()

"""
if __name__=='__main__':
    test_baidu_search_basic()
"""


    