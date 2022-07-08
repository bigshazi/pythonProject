#匿名函数
#返回最大值, lambda 匿名函数
max = lambda a,b : a if a>b else b
r = max(10,15)
if r != 15 :   #断言，如果r不等于10就报错
    raise AssertionError