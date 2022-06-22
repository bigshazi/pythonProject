import pymysql as pymysql
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time
import csv

# 搜索商品
def search_product(key_word):
    # 发送关键字
    wb.find_element(By.ID, 'q').send_keys(key_word)
    # 设定随机等待时间
    time.sleep(random.randint(1,3))
    # 最大化浏览器
    wb.maximize_window()
    # 点击跳转登录入口
    wb.find_element(By.XPATH,'//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[1]').click()
    # 输入账号名
    wb.find_element(By.ID, 'fm-login-id').send_keys(name)
    time.sleep(2)
    # 输入密码
    wb.find_element(By.ID, 'fm-login-password').send_keys(password)
    time.sleep(2)
    # 点击登录
    wb.find_element(By.XPATH, '//*[@id="login-form"]/div[4]/button').click()

    # 滚动滑条
    #login = wb.find_element(By.XPATH, '//*[@id="nc_1_n1z"]')
    #action = ActionChains(wb)
    #action.click_and_hold(on_element=login)
    #action.move_by_offset(xoffset=258, yoffset=0)滑动距离
    #action.pause(0.5).release().perform()  # perform()执行动作链
    #wb.find_element(By.XPATH, '//*[@id="login-form"]/div[4]/button').click()

    #登录等待时间
    time.sleep(2)
    # class前要加点,点击搜索按钮
    wb.find_element(By.XPATH,'//*[@id="J_TSearchForm"]/div[1]/button').click()

# 获取商品
def get_product():
    #注意要用elements去获取一个集合
    divs = wb.find_elements(By.XPATH,'//div[@class="items"]/div[@class="item J_MouserOnverReq  "]')
    for div in divs:
        # 标题
        info = div.find_element(By.XPATH,'.//div[@class="row row-2 title"]/a').text
        #价格
        price = div.find_element(By.XPATH,'.//strong').text+'元'
        #购买人数
        nums = div.find_element(By.XPATH,'.//div[@class="deal-cnt"]').text
        #店铺名称
        name = div.find_element(By.XPATH,'.//div[@class="shop"]/a').text
        #地址
        city = div.find_element(By.XPATH,'.//div[@class="location"]').text
        #打印数据
        print(info,price,nums,name,city)
        #保存
        with open('data.csv',mode='a',newline='',encoding='utf-8-sig')as file:
            csv_writer = csv.writer(file, delimiter=',')  # 指定分隔符
            csv_writer.writerow([info, price, nums, name])

def main():
    # 打开指定页面
    wb.get('https://www.taobao.com/')
    page = search_product(key_word)
    page_nums=1
    #爬取页数
    while page!= page_nums:
        print('*'*100)
        print("正在爬取{}页的信息".format(page_nums))
        wb.get('https://s.taobao.com/search?q={}&s={}'.format(key_word,page_nums))
        wb.implicitly_wait(10)  # 等待10秒
        get_product()
        page_nums +=1
def query(sql):
    # 连接数据库获取账号密码
    db = pymysql.connect(host='localhost',user='root',password='123456',db='new_schem',charset='utf8')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    #执行sql
    cursor.execute(sql)
    #获取查询结果
    data =cursor.fetchall()
    print(cursor.fetchmany(25))
    cursor.close()#关闭游标
    db.close()#关闭连接
    return data
#内置类名
if __name__ == '__main__':
    key_word =input("清输入你想爬取的关键字：")
    # 指定浏览器
    wb = webdriver.Chrome(r'D:\Win_TestEngineLite_20210120\chromedriver.exe')#r'D:\Win_TestEngineLite_20210120\chromedriver.exe'
    data= query("select * from student")
    for id,name,password in data:
        print(id,name,password)
    main()








