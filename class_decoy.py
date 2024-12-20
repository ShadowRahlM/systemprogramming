#! /usr/bin/python3.12


class MyClass(object):
    instance_count = 0

    def __init__(self, value):
        self.__value = value
        MyClass.instance_count += 1
        print("instance No {} created".format(MyClass.instance_count))
        # print('instance No,{MyClass.instance_count},created')

    def aMethod(self, aValue):
        self.__value *= aValue

    def __str__(self):
        return "A MyClass instance with value: " + str(self.__value)

    def __del__(self):
        MyClass.instance_count -= 1


one = MyClass(10)
one.instance_count
two = MyClass(50)
two.instance_count
MyClass.aMethod(one, 80)
print(two, one)
