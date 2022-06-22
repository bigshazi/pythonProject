# Author:hufei
names = "hufei xiayijin tangjinzhi"
names = ["hufei","xiayijin","tangjinzhi"]
names.append("youjiang")#追加一个名字
names.insert(1,"yili")#插入某个位置
names[2]='wenqiang'
nums=["hufei","xiayijin","tangjinzhi"]
del names[1]
names.pop()#将最后一个参数删除
names.reverse()#反转顺序
names.sort()#顺序排序
names.extend(nums)#将nums加在names后面
print(names)
print(names[1])
print(names[1:4]) #从1开始到4但不包括4的名字
print(names[-1])#切片
names2 = names.copy()
print(names2)

