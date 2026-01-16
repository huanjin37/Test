from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#显示等待
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_baidu_search_basic():
    driver =webdriver.Edge()
    #隐式等待
    driver.implicitly_wait(5)

    try:
        driver.get("https://baidu.com")
        print("已打开百度")
        time.sleep(3)

        
        
        search_input =driver.find_element(By.ID,'chat-textarea')
        search_input.send_keys('Selenium自动化测试')
        print("已在搜索框中输入关键词")
        time.sleep(3)

        search_button =driver.find_element(By.ID,'chat-submit-button')
        search_button.click()
        print("已点击按钮")

        time.sleep(2)

        assert "Selenium" in driver.title
        print ("测试通过！页面包含Selenium。")

        result_element =driver.find_element(By.PARTIAL_LINK_TEXT,"selenium")
        assert result_element is not None
        print("测试通过，找到包含selenium的链接")
        

    except Exception as e:
        print(f"测试过程出错：{e}")
        assert False,f"测试失败，原因：{e}"
    
    finally:
        print("测试结束")
        driver.quit()

if __name__=='__main__':
    test_baidu_search_basic()



    