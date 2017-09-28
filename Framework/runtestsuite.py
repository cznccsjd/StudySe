#coding:utf-8
'''
运行测试集
PyUnit使用TestRunner类作为测试用例的基本执行环境，来驱动整个单元测试过程。
Python开发人员在进行单元测试时一般不直接使用TestRunner类，而是使用其子类TextTestRunner来完成，
并将测试结果以文本方式显示出来
eg:
    runner = unittest.TextTestRunner()
    runner.run(suite)
'''

from selenium import webdriver
import unittest
from widget import Widget

#执行测试的类
class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget()
        print "this is setUp"

    def tearDown(self):
        self.widget.dispose()
        self.widget = None
        print "this si tearDown"

    def testSize(self):
        self.assertEqual(self.widget.getSize(),(40,40))
        print "this is testcase 'testSize'"

    def testResize(self):
        self.widget.resize(100,100)
        self.assertEqual(self.widget.getSize(),(100,100))
        print "this si testcase 'testResize'"

#测试
if __name__ == "__main__":
    #构造测试集
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase("testSize"))
    suite.addTest(WidgetTestCase("testResize"))

    #执行测试
    runner = unittest.TextTestResult()
    runner.run(suite)


'''
PyUnit模块中定义了一个名为main的全局方法，使用它可以很方便的将一个单元测试模块变成可以直接运行的测试脚本，
main()方法使用TestLoader类来搜索所有包含在该模块中的测试方法，并自动执行它们。
如果Python程序员能够按照约定（以test开头）来命名所有的测试方法，那就只需要在测试模块的最后加入如下几行代码即可：

#测试
if __name__ == "__main__":
    unittest.main()

'''