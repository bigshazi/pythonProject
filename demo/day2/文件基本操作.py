# Author:hufei
#将小说的任务写入文件中
fp=open('D:/text.txt','a+')#a+的作用是文件不存在就创建，存在就增加
print("文件输入字段 ",file=fp)
fp.close()