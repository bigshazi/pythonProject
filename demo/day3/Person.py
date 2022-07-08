#封装、继承、多态
class Person(): #封装
    def __init__(self):
        pass
    def set_name(self, name):
        self._name = name
    def get_name(self):
        return self._name
    def greet(self):
        print('hello world! Im {}'.format(self.name))

class Boy(Person):  #继承

    def run(self):
        print('i can run')

    def greet(self):
        print('i am subclass boy')


class Girl(Person): #多态

    def say(self):
        print('i can good girl')

    def greet(self):
        print('i am subclass Girl')

b = Boy()
b.name = '张三'
b.greet()
p = Person()
p.set_name('test')
print(p.get_name())
p.name='账' #使用format格式化的方法
p.greet()