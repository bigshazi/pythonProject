#断言函数
# assertEqual(a,b,msg=msg)：判断两个值是否相等；
# assertNotEqual(a,b,msg=msg)：上一函数的反义；
# self.assertTrue(a,msg=none)：判断变量是否为 True；
# assertFalse(a,msg=none)：同上反义；
# assertIsNone(obj=‘’)：判断 obj 是否为空；
# assertIsNotNone(obj=‘’)：同上反义；

# max = lambda a,b : a if a>b else b
# r = max(10,15)
# if r != 10 :   #断言，如果r不等于10就报错
#     raise AssertionError 增加断言报错·

def something():
    ""
    my_list = [] #申明一个空列表
    return  my_list

def func ():
    "调用something函数"
    ret = something()
    assert len(ret) == 18 #列表数量不对断言会报警
if __name__=="__main__":
    func()




