#比较大小
num_a=input('输入第一个数字：')
num_b=input('输入第二个数字：')
if num_a>=num_b:
    print(num_a,'大于等于',num_b)
else:
    print(num_a,'小于',num_b)
 #简化结构
print( str(num_a)+'大于等于'+str(num_b) if num_a>=num_b else str(num_a)+'小于'+str(num_b))
