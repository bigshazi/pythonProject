import  jenkins
name='hufei'


print(name)
print('标识',id(name))
print('类型',type(name))
print('值',name)

#浮点数
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))

#布尔类型
f1=True
f2=False
print(f1,type(f1))
print(f2,type(f2))

#python中布尔类型可转成数字
#True可转成数字1   False可转成0
print(1+f1)
print(1+f2)

name='hufei'
age=30
print('我叫'+name+'今年'+str(age))