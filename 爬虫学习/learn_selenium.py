from selenium import webdriver
driver_path = r"D:\Github\CPdotgithub\Python\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('http://www.baidu.com/')
print(driver.page_source)


"""selenium chan常用操作
    关闭当前页面 diver.close()
    关闭浏览器   driver.quit()


"""