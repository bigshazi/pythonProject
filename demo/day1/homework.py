# Author:hufei
# import day1 as pd
# df=pd.DataFrame({'ID':[1,2,3],'Name':['tom','sim','victor']})
# df.to_excel(r'C:\Users\胡飞\Desktop\test.xlsx')

username = {open()}
password = '123456'

_username = input("请输入用户名:",username)
_password = input("请输入密码:",password)
count =0
while count < 3:
    if _username == username and _password == password :
        print("认证成功！")
