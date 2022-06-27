import calendar
import time

ticks = time.time()
print("输出当前时间戳：" ,ticks )
localTime = time.localtime(ticks)
print("输出当前时间：",localTime)
print("输出当前格式化时间：",time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
print("输出日历：",calendar.month(2022,2))

