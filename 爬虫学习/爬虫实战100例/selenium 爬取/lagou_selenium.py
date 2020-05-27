# from selenium.webdriver import Chrome
# web = Chrome()
# web.get("http://www.baidu.com") 自动测试
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time 


web = Chrome()
web.get("https://www.lagou.com/") 

web.find_element_by_xpath('//*[@id="cboxClose"]').click()
time.sleep(1)
web.find_element_by_xpath('//*[@id="search_input"]').send_keys('python',Keys.ENTER)
time.sleep(1)
web.find_element_by_xpath('/html/body/div[8]/div/div[2]').click()

alist = web.find_elements_by_xpath('//*[@id="s_position_list"]/ul/li/div[1]/div[1]/div[1]/a/h3')[:]#取值范围
print(alist)
# for a in alist:
#     a.click()
#     time.sleep(1)
#     web.switch_to.window(web.window_handles[-1])
#     job_info = web.find_element_by_xpath('//*[@id="job_detail"]/dd[2]').text
#     print(job_info)
#     print('='*40)
#     web.close()
#     web.switch_to.window(web.window_handles[0])
#     time.sleep(1)
