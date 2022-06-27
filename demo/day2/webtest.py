
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# #创建webDriver对象，指定浏览器驱动
# wb = webdriver.Chrome(r'D:\Win_TestEngineLite_20210120\chromedriver.exe')
# #打开对应页面
# wb.get('https://sf.taobao.com/?spm=a21bo.jianhua.201859.4.315f11d96oKZ9O')
# #获取元素
# elements = wb.find_element(By.CLASS_NAME,'left-nav-link')
# #点击切换到珍品tab
# #element.click()
# #获取搜索结果
# for element in elements:
#     print(element.text)

from selenium import webdriver
from selenium.webdriver.common.by import By

# 加上参数，禁止 chromedriver 日志写屏
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
wd = webdriver.Chrome(r'D:\Win_TestEngineLite_20210120\chromedriver.exe',options=options)
#设置最大等待时间10秒
wd.implicitly_wait(10)
wd.get('https://www.baidu.com')

wd.find_element(By.ID, 'kw').send_keys('白月黑羽\n')
#等待2秒
from time import sleep
sleep(2)


# 现在搜索结果在百度页面上，有2个ID为1 的元素，它是第2个
elements = wd.find_elements(By.ID,'1')
# #获取class元素的属性值
print(wd.find_element(By.ID,'kw').get_attribute('class'))

print(elements[1].text)

#清掉搜索词
wd.find_element(By.ID,'kw').clear()
wd.find_element(By.ID,'su').click()
#关闭浏览器
wd.quit()