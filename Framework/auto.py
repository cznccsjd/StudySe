#coding:utf-8

from widget import Widget
import unittest

#执行测试的类
class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget()

    def testSize(self):
        self.assertEqual(self.widget.getSize(),(40,40))

    def tearDown(self):
        self.widget = None

#构造测试集
#定义一个全局函数suite(),作为整个单元测试的入口，PyUnit通过调用它来完成整个测试过程
def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase("testSize"))
    return suite

#测试
if __name__ == '__main__':
    unittest.main(defaultTest = 'suite')
