import calendar
import time

ticks = time.time()
print("输出当前时间戳：" ,ticks )
localTime = time.localtime(ticks)
print("输出当前时间：",localTime)
print("输出当前格式化时间：",time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
print("输出日历：",calendar.month(2022,2))

# 今天 today = datetime.date.today()
# 昨天 yesterday = today - datetime.timedelta(days=1)
# 上个月 last_month = today.month - 1 if today.month - 1 else 12
# 当前时间戳 time_stamp = time.time()
# 时间戳转datetime datetime.datetime.fromtimestamp(time_stamp)
# datetime转时间戳 int(time.mktime(today.timetuple()))
# datetime转字符串 today_str = today.strftime("%Y-%m-%d")
# 字符串转datetime today = datetime.datetime.strptime(today_str, "%Y-%m-%d")
# 补时差 today + datetime.timedelta(hours=8)

#秒表功能
#round(time.time()-starttime,0)0指的是保留几位小数
print('按下回车开始计时，按下 Ctrl + C 停止计时。')
while True:
    input('')
    starttime = time.time()#生成当前时间戳
    print('开始')
    try:
        while True:
            print('计时',round(time.time()-starttime,0),'秒',end="\r")
            time.sleep(1)
    except KeyboardInterrupt:
        print('结束')
        endtime = time.time()
        print('总共的时间为:', round(endtime - starttime, 2),'secs')
        break

