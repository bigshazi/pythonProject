# Author:hufei
print("="*50)
print("            名字管理系统 V8.6")
print(" 1:添加一个新的名字")
print(" 2:删除一个名字")
print(" 3:修改一个名字")
print(" 4:查询一个名字")
print(" 0:退出该程序")
print("="*50)

names =["小仙女","阿童木","二硕","小姑凉"]

while True :
    num =   int(input("请输入功能号："))
    if   num==1 :
        name = input("请输入你想要添加的名字：")
        names.append(name)
    elif num==2:
        name=input("请输入你想删除的名字：")
        names.remove(name)
    elif num==3:
        name =input("请输入你想修改的名字：")
        if name in names:
            names.remove(name)
            name2=input("请输入你想修改成的名字：")
            names.append(name2)
        else:
            print("不好意思，查无此人！")
    elif  num==4:
        name =input("请输入你想查询的名字：")
        if name in names :
            print("系统中存在此人")
        else :
            print("系统查无此人")
    elif num==0:
        print("感谢你的使用！")
        break
    else:
        print("输入错误！！！")
    print(names)
