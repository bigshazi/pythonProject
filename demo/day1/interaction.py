# Author:hufei
import random

username = input("username:")
password = input("password:")
print(username,password)
name = input("name:")
age = int(input("age:"))#强转integer
print(type(age)) #打印数据类型
job = input("job:")
salary = input("salary:")
info = '''---info of %s---
    Name:%s
    Age:%d
    Job:%s
    Salary:%s
'''%(name,name,age,job,salary)

info2 = '''---info of {name}---
Name:{name}
Age:{age}
Job:{job}
Salary:{salary}
'''
print(info2)
print(random.random())#0-1之间得随机数
print(random.randint(1,100))#1-100之间随机数
