#文件读取函数

file = "D:\pythonProject\demo\day1\long.txt" #非同一层目录需要填写完整地址
with open(file,'rb') as f:
    data =f.read()
    print(data)


class Animal:
    def __enter__(self):
        print("__enter__()")

    def __exit__(self, type, value, trace):
        print("__exit__()")


with Animal() as animal:
    pass