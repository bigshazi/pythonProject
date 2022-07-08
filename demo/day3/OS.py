import os
#获取系统名称
print(os.name)
#获取当前工作目录 ；
print(os.getcwd())
#执行命令：
#os.system(‘命令行’)
# 文件和文件夹相关：
# os.remove(path) 删除指定的文件
# os.rename(src,dest) 重命名文件或目录
# os.stat(path) 返回文件的所有属性
# os.listdir(path) 返回path目录下的文件和目录列表
# os.mkdir(path) 创建目录
# os.makedirs(path1/path2/path3/…) 创建多级目录
# os.rmdir(path) 删除目录
# os.removedirs(path1/path2/path3/…) 删除多级目录
# 路径相关函数：
# os.path.isabs(path) 判断path是否是绝对路径
# os.path.isdir(path) 判断path是否为目录
# os.path.isfile(path) 判断path是否为文件
# os.path.exists(path) 判断指定路径的文件是否存在
# os.path.getsize(filename) 返回文件大小
# os.path.abspath(path) 返回绝对路径