#test类
import time


class data():
    count=0
    type ='ren' #静态字段
    def __init__(self, year, month, day):
        self._year = year
        self._month = month
        self._day = day
    #普通方法
    def set_day(self, day):
        self._day = day
    #用于装饰“类方法”。需要参数cls，无需self。该类方法可以直接被调用，而无需实例化。无self 参数，也无法访问实例化后的对象该类方法只能访问类属性，而无法访问实例属性。
    @classmethod
    def today(cls):
        todayBackup =time.localtime()
        return cls(todayBackup.tm_year,todayBackup.tm_mon,todayBackup.tm_mday)
    @classmethod
    def get(cls):
        return  cls.count
    #静态方法。无需参数cls、self。被装饰的方法会成为静态方法，无需实例化可以调用
    @staticmethod
    def static_func():
        print('静态方法')
    #将函数封装为属性。需要参数self，实例对象直接调用该方法，无需()。
    @property
    def printtime(self):
        return str(self._year)+'-'+str(self._month)+'-'+str(self._day)
today = data.today() #先调用生成本地时间戳 先实例化
print(today.printtime) #再调用格式化时间并输出

