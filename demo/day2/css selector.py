from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome(r'D:\Win_TestEngineLite_20210120\chromedriver.exe')

wd.get('http://cdn1.python3.vip/files/selenium/sample1.html')
#id前要加#
element = wd.find_element(By.CSS_SELECTOR, '#searchtext')
element.send_keys('你好')
#class前要加点
elements =wd.find_elements(By.CSS_SELECTOR,'.animal')
element =wd.find_element(By.CSS_SELECTOR,'[href="http://www.miitbeian.gov.cn"]')
print(element.get_attribute('outerHTML'))
print(elements)

#等待2秒
from time import sleep
sleep(2)
#关闭页面
wd.quit()