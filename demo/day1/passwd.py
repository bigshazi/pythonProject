# Author:hufei
import getpass #导入密文模块
_username ='hufei'
_password = '123456'
username = input("username:")
#assword = getpass.getpass("password:") #只能在python dos模式下使用
password = input("password:")
if _username == username and _password == password:
    print("Welcome user {name} login...".format(name=username))
else:
    print("密码或账号名错了！")
print(username,password)