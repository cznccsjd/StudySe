#coding:utf-8
'''
组织用例集
完整的单元测试很少只执行一个测试用例，开发人员通常都需要编写多个测试用例才能对某以软件功能进行比较完整的测试，
这些相关的测试用例成为一个测试用例集，在PyUnit中用TestSuite类来表示的
可以在单元测试代码中定义一个名为suite()的全局函数，并将其作为整个单元测试的入口，PyUnit通过调用它来完成整个测试过程；
'''
import unittest
from edit import WidgetTestCase


def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase("testSize"))
    suite.addTest(WidgetTestCase("testResize"))
    return suite

#   如果用于测试的类中所有的测试方法都以test开头，Python程序员甚至可以用PyUnit模块提供的makeSuite()方法来构造一个。
def suite():
    return unittest.makeSuite(WidgetTestCase, "test")

#   TestSuite类可以看成是TestCase类的一个容器，用来对多个测试用例进行组织，这样多个测试用例可以自动在一次测试中全部完成