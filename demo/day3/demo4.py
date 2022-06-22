#函数\
r=range(1,10)
print(r)
print(list(r))
print(range(1,20,1))
#循环结构
a=0
while a<=10:
    print(a)
    a+=1
#求和
b=0
sum=0;
while b<5:
    sum+=b
    b+=1
    print(sum)
#计算1到100之间的偶数和
sum=0
a=1
while a<=100:
    if a%2==0:
       sum+=a
    a+=1
print(sum)
#for in遍历
for i in range(10):
    print(i)
#_为空，输入5次‘人生苦短’
for _ in range(5):
    print('人生苦短')
#计算1到100之间的偶数值
sum=0
for i in range(101):
    if i%2==0:
        sum+=i
    i+=1
print(sum)




