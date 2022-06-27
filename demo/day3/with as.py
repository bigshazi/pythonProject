#文件读取函数

file = "D:\pythonProject\demo\day1\long.txt"
with open(file,'rb') as f:
    data =f.read()
    print(data)