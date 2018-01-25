
#encoding:utf-8
#学习类和实例
#1、python中初始化实例属性
#必须在__init__(self,…)方法内(注意：双下划线)初始化实例，第一个参数必须为self。
class Person(object):
    def __init__(self,name,gender,birth,**kw):
        self.name = name
        self.gender = gender
        self.birth = birth
        for k,v in kw.iteritems() :
            setattr(self,k,v)
xiaoming = Person('Xiao Ming', 'Male', '1990-1-1', job='Student')
print xiaoming.name
print xiaoming.job


#Python对属性权限的控制是通过属性名来实现的，如果一个属性由双下划线开头(__)，该属性就无法被外部访问。

#如果一个属性以"__xxx__"的形式定义，那它又可以被外部访问了，以"__xxx__"定义的属性在Python的类中被称为特殊属性，有很多预定义的特殊属性可以使用，通常我们不要把普通属性用"__xxx__"定义。

#以单下划线开头的属性"_xxx"虽然也可以被外部访问，但是，按照习惯，他们不应该被外部访问。
class Person(object):
    def __init__(self, name):
        self.name = name
        self._title = 'Mr'
        self.__job = 'Student'
p = Person('Bob')
print p.name
# => Bob
print p._title
# => Mr
#print p.__job#会报错

#3、python中创建类属性

#实例属性每个实例各自拥有，互相独立，而类属性有且只有一份。
class Person(object):
    count = 0

    def __init__(self, name='Smith'):
        Person.count = Person.count + 1
        self.name = name


p1 = Person('Bob')
print Person.count

p2 = Person('Alice')
print Person.count

p3 = Person('Tim')
print Person.count
#注意，python不支持构造函数的重载。但通过设置默认值，调用构造函数时就可以省略参数。
p4 = Person()
print Person.count


class Person(object):
    address = 'Earth'

    def __init__(self, name):
        self.name = name


p1 = Person('Bob')
p2 = Person('Alice')

print 'Person.address = ' + Person.address
#Person.address = Earth
p1.address = 'China'
print 'p1.address = ' + p1.address
#p1.address = China

print 'Person.address = ' + Person.address
#Person.address = Earth
print 'p2.address = ' + p2.address
#p2.address = Earth

#5、python中定义实例方法

#类实例方法的定义在类体中，第一个参数必须是self，调用时无需显示传入
class Person(object):
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


a = Person("Jim")
a.get_name()
#6、python中方法也是属性
import types


def fn_get_grade(self):
    if self.score >= 80:
        return 'A'
    if self.score >= 60:
        return 'B'
    return 'C'


class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score


p1 = Person('Bob', 90)
p1.get_grade = types.MethodType(fn_get_grade, p1, Person)
print p1.get_grade()
# => A
p2 = Person('Alice', 65)
#print p2.get_grade() 报错语句
# ERROR: AttributeError: 'Person' object has no attribute 'get_grade'
# 因为p2实例并没有绑定get_grade

#7、python中定义类方法
#通过 @ classmethod语句将方法绑定到Person类上。
#类方法中不用self，使用cls代指类。

class Person(object):
    __count = 0

    @classmethod
    def how_many(cls):
        return cls.__count

    def __init__(self, name):
        Person.__count += 1
        self.name = name


print Person.how_many()
p1 = Person('Bob')
print Person.how_many()