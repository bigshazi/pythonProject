#字符串的一些函数
#find函数
my_str="测试find函数"
print(my_str.find('f'))#输出的是字符所在的位置
#title函数
my_str2='abadaeafb'
print(my_str2.title())#输出的字符串首字母是大写
#upper全大写，lower全小写
print(my_str2.upper())#全大写
print(my_str2.lower())#全小写
my_str3=' abcdef '
#strip去掉空格
print(my_str3.strip())#去掉空格
#count统计数量
print('abcaaabbbcccdddd'.count('a'))
#endswith和startswith
print(my_str2.endswith('d'))#以d结尾返回布尔类型
print(my_str2.startswith('c'))#以c开头返回布尔类型
#replace()替换函数
print(my_str2.replace("a","b",2))#替换不超过2次
#format格式化
my_str = "小爱同学，今天天气"
answer_str = "今天的天气是： {}".format("晴")
print(answer_str) #根据括号自动填充字符串

