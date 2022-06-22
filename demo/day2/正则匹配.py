#原生字符串，处理\n被解析成换行
my_str=r'C:\number'
print(my_str)
#位置函数
def describe_student(person_name,student_age='18'):
    "函数功能：显示学生信息"
    print("my name is ",person_name)
    print(person_name+" is "+student_age+" years old")
#调用函数
describe_student('jack','24')
#调用参数并使用默认值
describe_student('jack')


def test_add(H=None):
    if H is None:
        H = []
    H.append('END')
    return H
print(test_add())
print(test_add())