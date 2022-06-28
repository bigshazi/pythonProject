
def get_input():
    input_string = input('请输入由逗号隔开的数字：')
    a,b = input_string.split(',')
    try:
        float(a)
        float(b)
        return int(a),int(b)
    except ValueError :
        pass
    print(b,type(b))

def num(a,b):
    try:
        num3 = a / b
    except ZeroDivisionError :
        print("除数不可以为 0 ")
    except TypeError :
        print("除数类型不对")
    else:
        print("无异常，直接执行"+'\n',num3)

def run():
    a,b = get_input()
    num(a,b)
if __name__ == '__main__'  :
    run()
