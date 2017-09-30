#coding:utf-8
"""
使用测试套件来执行多个.py测试文件，最终测试套件完成下面的结构：
                     ---------------
                    |  执行用例集  |
                    |(测试套件.py)|
                    --------------
                    /         |                     
          -------------    -------------       -------------
         | 测试文件一 |   | 测试文件二 |      | 测试文件...|
        |    (.py)   |   |(.py)        |     | (.py)      |
        -------------    -------------       -------------
            |     |
         用例1   用例2        用例3   用例4       用例5  用例6
        (方法)   (方法)       (方法)  (方法)     (方法) (方法)
"""

######### 设计测试文件：test_youdao.py 、 test_baidu.py

import unittest
import time, test_baidu, test_youdao,HTMLTestRunner
#罗列要执行的文件
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(test_youdao.youdao,'test'))
suite.addTest(unittest.makeSuite(test_baidu.Baidu,'test'))
#执行测试用例

#############   不用HTMLTestRunner
#runner = unittest.TextTestRunner()
#runner.run(suite)

#############   使用HTMLTestRunner
time
filename = r"D:\\Documents\workspace\studySE\Report\testSuite_report1709301544002.html"
fp = open(filename, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试套件的测试报告', description=u'这个测试报告，存放的是测试套件运行结果')
runner.run(suite)
