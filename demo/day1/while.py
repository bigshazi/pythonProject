# Author:hufei
# count = 0
# while True:
#     print("count:",count)
#     count = count + 1 #count +=1
#     if count == 1000:
#         break

# for i in range(0,10,2):  #(start, stop[, step]) 计数从 start 开始，计数到 stop 结束，step 步长
#     print("loop",i)

# for i in range(0,10):
#     if i < 3:
#         print("loop",i)
#     else:
#         continue
#     print("hehe...")

for i in range(0,10):
    print('----',i)
    for j in range(0,10):
        print(j)
        if j >5:
            break

