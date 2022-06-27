# Author:hufei
# -*- coding: utf-8 -*-
import logging
def out_file():
    oldfile = "long.txt"  # 需要去重的文件
    with open(oldfile, 'rb') as f:
        with open("result.txt", "a+",encoding="utf-8-sig") as g:
            for line in f.read().decode().split('},'): #分行
                    if key_word not in line:
                        g.write(line + "\n")
                        print(line)
    f.close()
    logging.info("*******")
    g.close()
    logging.info("*******")
if __name__ =="__main__":
    key_word = input("清输入你想去掉的关键字：")
    out_file()

