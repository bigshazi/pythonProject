#输出100到999之间的水仙花数

for item in range(100,1000):
    ge=item%10      #个位
    shi=item//10%10 #十位
    bai=item//100   #百位

    if ge**3+shi**3+bai**3==item:
        print(item)

#输入密码，最多三次，正确则结束循环 break
for pwd in range(3):
    pwd=input("请输入密码：")
    if pwd=="888":
        print("密码正确")
        break
    else:
        print("密码错误")

#break
a=0;
while a<3:
        pwd2=input("请输入密码：")
        if pwd2=="8888":
            print("密码正确")
            break
        else:
            print("密码错误")
        a+=1
#continue
#要求输出5的倍数
for item in range(1,51):
    if item%5!=0:
        continue
    print(item)

#输入长度大于3的名字
names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
for name in [names]:
    if len(name)<=3:
        print([name])
new_names=[name.upper()]
print(new_names)
