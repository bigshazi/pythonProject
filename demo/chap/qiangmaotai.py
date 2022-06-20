# encoding=utf-8
# init就是所有USB连接电脑的手机上都安装uiautomator2
#python -m uiautomator2 init
# 指定手机安装uiautomator2， 用 --mirrorpip list | findstr weditor

#python -m uiautomator2 init --mirror --serial $SERIAL
# 嫌弃慢的话，可以用国内的镜像
#python -m uiautomator2 init --mirror

#安装pip install weditor==0.6.4

from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey
#开启cmd 获取运行appPackage和Activityadb命令 shell dumpsys window | findstr mCurrentFocus
desired_caps = {
  'platformName': 'Android', # 被测手机是安卓
  'platformVersion': '10.0.0', # 手机安卓版本
  'deviceName': 'test', # 设备名，安卓手机可以随意填写
  'appPackage': 'com.moutai.mall', # 启动APP Package名称
  'appActivity': 'com.moutai.mall.module.login.LoginActivity', # 启动Activity名称
  'unicodeKeyboard': True, # 使用自带输入法，输入中文时填True
  'resetKeyboard': True, # 执行完程序恢复原来输入法
  'noReset': True,       # 不要重置App
  'newCommandTimeout': 6000,
  'automationName' : 'UiAutomator2'
  # 'app': r'd:\apk\bili.apk',
}

# 连接Appium Server，初始化自动化环境
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 设置缺省等待时间
driver.implicitly_wait(5)

# 如果有`青少年保护`界面，点击`我知道了`
#iknow = driver.find_element("text3")
#if iknow:
#    iknow.click()

# 根据id定位搜索位置框，点击
driver.find_element("com.moutai.mall:id/tab_name", text="小茅运").click()
#点击旅行icon
driver.find_element()


# 根据id定位搜索输入框，点击
sbox = driver.find_element('search_src_text')
sbox.send_keys('白月黑羽')
# 输入回车键，确定搜索
driver.press_keycode(AndroidKey.ENTER)

# 选择（定位）所有视频标题
eles = driver.find_element("title")

for ele in eles:
    # 打印标题
    print(ele.text)

input('**** Press to quit..')
driver.quit()