# Author:hufei
#python3中需要转成二进制
msg = 'hello，你好'#表示为utf-8
print(msg.encode(encoding="utf-8")) #转成二进制
print(msg.encode(encoding="utf-8").decode(encoding="utf-8"))#再转成utf-8
