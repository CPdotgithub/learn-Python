from selenium import webdriver
from selenium.webdriver.common.keys  import Keys
import time

driver = webdriver.Chrome()
driver.get("https://money.163.com/")
#点击进入A股
driver.find_element_by_xpath('//*[@id="index2016_wrap"]/div/div[3]/div[2]/div[3]/div[1]/div/ul[1]/li[1]/a').click()

time.sleep(1)
driver.switch_to.window(driver.window_handles[-1])
for a in range(1,72):
        
    js = 'document.querySelector("#sidebar-nav-tabs > ul > li.tab-panel.panel.panel-blank-head.active > div > ul > li:nth-child(%d) > a")'%a
    print(js)
    driver.execute_script(js)




