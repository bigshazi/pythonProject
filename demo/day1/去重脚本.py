# Author:hufei
# -*- coding: utf-8 -*-
import re
#
# list01 =[];
# list02 =[];
# file = '/demo/day1/long.txt'
# f = open(r"long.txt", "rb")
# str =f.readlines()
# with
#
# for line in str :
#     print(str)
#     out_file=set()
#     list02 = line.split("locationCode",2)
#     print(list02)
#     if line in list01:
#         continue
#     list01.append(line)
#     list02 = list01.split()
#     f.close()
# print(list02)
#

file_list =[] #创建空列表
def out_file():
    file = "long.txt" #需要去重的文件
    with open(file,'rb') as f:
        file_2 = f.read().decode().split('},')
        for file in file_2:
            file_list.append(file)
        out_file1 =set(file_list)#set()函数可以自动过滤掉重复元素
        last_out_file = list(out_file1)
        for out in last_out_file:
            with open("result.txt", "a+") as f:  # 去重后文件写入文件里
                f.write(out + "\n")
                print(out)

if __name__ =="__main__":
    out_file()
