#coding:utf-8
'''
编写测试用例
采用PyUnit提供的动态方法，只编写一个测试类来完成对整个软件模块的测试，
这样对象的初始化工作可以在setUP()方法中完成，而资源的释放则可以在tearDown()方法中完成

我们可以在一个测试类中，写多个测试用例对被测试类的方法进行测试
'''
import unittest
from  widget import Widget
from selenium import webdriver

##########  对widget.py被测试类的多方法进行测试
class WidgetTestCase(unittest.TestCase):

    def setUp(self):
        self.widget = Widget()
        print "this is setup"

    #测试getSize()方法的测试用例
    def testSize(self):
        self.assertEqual(self.widget.getSize(),(40,40))
        print "this is first test"

    #测试resize()方法的测试用例
    def testResize(self):
        self.widget.resize(100,100)
        self.assertEqual(self.widget.getSize(),(100,100))
        print "this si second test"

    def tearDown(self):
        self.widget.dispose()
        self.widget = None
        print "this is tearDown"

if __name__ == '__main__':
    print "这个if有问题，就别执行了，光看代码吧，而且忽略print吧"