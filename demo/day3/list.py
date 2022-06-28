nn_list = [(x,y,z,m) for x in range(3) for y in range(3) for z in range(3) for m in range(3)]
print(nn_list)
#推导式写法节约运行速度
import time
def demo1():
    new_list = []
    for i in range(10000000):
        new_list.append(i*2)

def demo2():
    new_list = [i*2 for i in range(10000000)]

s_time = time.perf_counter()
demo1()
e_time = time.perf_counter()

f_time=time.perf_counter()
demo2()
m_time=time.perf_counter()
print("demo1代码运行时间：", e_time-s_time)
print("demo2代码运行时间：",m_time-f_time)

#返回最大值, lambda 匿名函数
max = lambda a,b : a if a>b else b
r = max(10,15)
if r != 15 :   #断言，如果r不等于10就报错
    raise AssertionError
