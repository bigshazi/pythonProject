#条件表达式
#单分支结构
money =1000 #余额
s=int(input('请输入取款金额:'))
if money >=s:
    money=money-s #余额
    print('取款成功，余额为:', money )

num =int(input('输入一个数字:'))
#双分支结构
if num%2==1:
    print('这个数字是奇数')
else:
    print('这个数字是偶数')
#多分支结构
score =int(input('输入成绩：'))
if 90<=score<=100:
    print('你的成绩等级为：A')
elif 80<=score <=89:
    print('你的成绩等级为：B')
elif 70<=score<=79:
    print('你的成绩等级为：C')
elif 0<=score<=59:
    print('考的太差了')
else :
    print('成绩有问题')
#嵌套if
answer=input('你是会员？y/n')
money=float(input('请输入你的购物金额：'))
if answer=='y':
    if money>=200:
        print('打8折，付款金额为：',money*0.8)
    elif money>=100:
        print('打九折，付款金额为：',money*0.9)
    else:
        print('不打折，付款金额为：',money)
else:
    if money>=200:
        print('打9.5折，付款金额为：',money*0.95)
    else:
        print('不打折，付款金额为：',money)