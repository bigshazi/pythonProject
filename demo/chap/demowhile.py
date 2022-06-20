#循环
n =100;
sum=0;
center =1;
while center<=n:
    sum = sum + center;
    center += 1;
    print(sum)
#for循环
name =['a','b','c']
for x in name:
    print(x)

sites = ["Baidu","Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print('测试')
        break
    print('循环数据'+ site)
else:
    print("没有循环数据")
print("完成循环！")
#range函数
i=0
for  i in range(5):
    print(i)
#break
for letter in 'Runoob':  # 第一个实例
    if letter == 'b':
        break
    print('当前字母为 :', letter)

var = 10  # 第二个实例
while var > 0:
    print('当前变量值为 :', var)
    var = var - 1
    if var == 5:
        break
print("Good bye!")
