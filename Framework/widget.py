#coding:utf-8

#将要被测试的类
class Widget:
    def __init__(self, size = (40,40)):
        self.__size = size

    def getSize(self):
        return self.__size

    def resize(self,width,height):
        if width < 0 or height < 0:
            raise ValueError, "illegal size"
        self.__size = (width, height)

    def dispose(self):
        pass