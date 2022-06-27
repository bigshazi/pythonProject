
def get_input():
    input_string = input('请输入由逗号隔开的数字：')
    a_string,b_string = input_string.split(',')
    return a_string,b_string
def num(a,b):
    try:
        num3 = a / b
        return num3
    except ZeroDivisionError :
        print("除数不可以为 0 ")
    except TypeError :
        print("除数类型不对")
    else:
        print("无异常，直接执行"+'\n',num3)

def run():
    a,b = get_input()
    num(a,b)
run()
