#输入函数结果是str类型
present=input('大圣你想要什么礼物呢？')
print(present,type(present))
#转换之后数字相加
a=input('请输入一个加数：')
b=input('请输入另一个数：')
print(int(a)+int(b))
#运算方法
print(1+1)#加法运算
print(1-1)#减法运算
print(2*4)#乘法运算
print(1/2)#除法运算
print(11//2)#整除运算
print(11%2)#取余运算
print(2**2)#表示2的2次方
print(2**3)#表示2的3次方

print(9//-4)#一正一负的整数公式，向下取整 -3

print(9%-4)#-3 公式：余数=被除数-除数*商 9-（-4）*（-3） 9-12=-3
print(-9%4)#3  公式：                 -9-4*（-3）  -9+12=3
#赋值运算符 运算顺序从右到左
i=3+4
print(i)
a=b=c=20 #链式赋值
#支持参数赋值
a=20
a+=30
print(a)
#解包赋值
a,b,c=20,30,40
print(a,b,c)
#交换
a,b=10,20
a,b=b,a
print(a,b)

#比较运算符
a=10
b=10
print(a==b)#说明a与b的value相等
print(a is b)#说明a与b的id标识相等
#列表在比较时标识id会不同
list1=[11,22,33,44]
list2=[11,22,33,44]
print(id(list1))
print(id(list2))
print(list1==list2) #true
print(list1 is list2) #false
print(list1 is not list2) #true

#布尔运算
a=1
b=2
print(a!=1 and b!=2) #false
print(a==1 or b==2 )
#not对bool类型操作数取反
f1=True
f2=False
print(not f1)
#in 与not in
s='helloworld'
print('w'in s)
print('w' not in s)
print(4&8)#按位与&，同为1时结果为1
print(4|8)#按位或|，同为0时结果为0
















