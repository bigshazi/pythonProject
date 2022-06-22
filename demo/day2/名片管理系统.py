# Author:hufei
print("*"*50)
print("             名片管理系统  V0.01")
print("1:添加一个新的名片")
print("2:删除一个名片")
print("3:修改一个名片")
print("4:查询一个名片")
print("5:打印所有名片")
print("0:退出系统")
print("*"*50)

members =[{"name":"小仙女", "age":"18", "qq":"1234", "address":"合肥"}]
while True:
    num = int(input("请输入对应功能号："))
    if num ==1:
        n_name =input("请输入新的名字：")
        n_age  =input("请输入年龄：")
        n_qq   =input("请输入QQ号：")
        n_address =input("请输入地址：")
        infor ={}
        infor["name"]=n_name
        infor["age"]=n_age
        infor["qq"]=n_qq
        infor["address"]=n_address
        members.append(infor)
        print("姓名 \t年龄 \tqq \t地址")
        for temp in members:
            print("%s\t%s\t%s\t%s" % (temp["name"], temp["age"], temp["qq"], temp["address"]))
    elif num ==2:
        person =input("请输入你想删除的名片：")
        members.remove(person)
        print(members)
    elif num ==3:
        person =input("请输入你想修改的名片：")
        members.remove(person)
        person2 =input("请输入修改后的名片：")
        members.append(person2)
        print(members)
    elif num == 4:
        name = input("请输入你想查询的名字：")
        name_flag = 0
        for temp in members:
            if temp["name"] == name :
                name_flag = 1
                break
        if name_flag ==0:
            print("查无此人")
    elif num == 5:
        print("姓名 \t年龄 \tqq \t地址")
        for temp in members:
            print("%s\t%s\t%s\t%s" % (temp["name"], temp["age"], temp["qq"], temp["address"]))
    elif num == 0:
        print("感谢你的使用！")
        break
    else:
        print("输入错误，请重新输入！！！")
    print("")


print(range(10));