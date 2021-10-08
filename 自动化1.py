''''''
    #做自动化的前提条件
    #1.需求变更的不是特别频繁，系统功能更新也不是特别频繁。
    #2.适用于系统趋于稳定性，需求变更不是很频繁的情况下。

    #1.环境:

        #selenium
        #chromeDriver.exe

        #谷歌浏览器：【IE(6,8,9,10)，谷歌，火狐】
import time

''''''

from selenium import  webdriver

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")

driver.maximize_window()

driver.find_element_by_id("kw").send_keys("JD.com")

driver.find_element_by_id("key").send_keys("item.jd.com/")

driver.find_element_by_id("su").click()





#time.sleep(10)

#driver.quit()











