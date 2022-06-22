#format函数使用
import math
PI = math.pi   #PI --> 3.141592653589793
val = -2018.1229
#保留小数点后2位 ： {:.2f}
print('{0:.2f}  {1:.2f}'.format(PI,val))
#带符号保留小数点后两位 : {:+.2f}
print('{0:+.2f} {1:+.2f}'.format(PI,val))
#舍弃小数 : {:.0f}
print('{0:.0f} {1:.0f}'.format(PI,val))
#增加千位分隔符–> {:,}
print('{0:,}'.format(10000000))
#设置宽度为6,左填充 --> {0:*>6d} 宽度为6,右填充x --> {1:x<6d}
print('{0:*>6d} {1:x<6d}'.format(2018,2019) )
#转成百分比格式 --> {:.2%} ,指数格式 : {:.2e}
print('{0:.2%} {1:.2e}'.format(0.25,10000000))
#设置对齐 : <左对齐 >右对齐 ^居中
print('{0:*<10d} {1:*<10d}'.format(2018,1229)) #左对齐
print('{0:*^10d} {1:*^10d}'.format(2018,2019)) #居中
print('{0:*>10d} {0:*>10d}'.format(2018,2019))#右对齐
#进制转换
#{:d} --> 十进制,
#{:b} --> 二进制,
#{:#b} --> 带前缀二进制,
#{o} --> 八进制,
#{:#o} --> 带前缀八进制,
#{:x} --> 十六进制
#{:#x}–> 带前缀十六进制
#{:#X} --> 带前缀大写十六进制
#用bin()转二进制会带有前缀0b,但format()不会
d2b = bin(255)
use_format = format(255,'b')
print(d2b +'      '+use_format)  #输出： 0b11111111      11111111

print('{:d}'.format(255))    #255
print('{:b}'.format(255))    #11111111
print('{:#b}'.format(255))   #0b11111111
print('{:o}'.format(255))    #377
print('{:#o}'.format(255))   #0o377
print('{:x}'.format(255))    #ff
print('{:#x}'.format(255))   #0xff
print('{:#X}'.format(255))   #0XFF