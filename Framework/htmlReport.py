#coding:utf-8
'''
用例中生成可以添加测试报告的代码
'''
from selenium import webdriver
import unittest,time
import HTMLTestRunner

class Baidu(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Firefox()
        self.dr.implicitly_wait(10)
        self.base_url = "http://www.baidu.com"
        self.verificationErrors = []
        self.accept_next_alert = True

    #测试用例一
    def test_baidu_One(self):
        print "this is the first testcase"

    #测试用例二
    def test_baidu_Two(self):
        print "this is the second testcase"

    #测试用例三
    def test_baidu_Three(self):
        print "this is the third testcase"

    def tearDown(self):
        time.sleep(2)
        self.dr.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
#if __name__ == "htmlReport":
    #定义一个单元测试容器
    testUnit = unittest.TestSuite()
    #将测试用例加入到测试容器中
    testUnit.addTest(Baidu("test_baidu_One"))
    testUnit.addTest(Baidu("test_baidu_Two"))
    testUnit.addTest(Baidu("test_baidu_Three"))

    #定义保存存放路径，支持相对路径
    filename = r'D:\Documents\workspace\studySE\Report\result170928185201.html' #其他电脑运行时，注意修改路径
    fp = open(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream = fp, title = 'Report_title_170928185201',description = 'Report_description for myself')
    #自动进行测试
    runner.run(testUnit)
    #unittest.main(testUnit)    #用来测试unittest测试用例没有问题
    #关闭报告文件
    fp.close()
    '''
    41-46行，创建result.html文件，给以读写权限（wb），调用HTMLTestRunner文件，并将测试结果以HTMLTestRunner规定的格式
    通过fp传递写到result.html文件中。
    最后运行testUnit，也就是TestSuite中的所有用例
    ############## 使用pycharm不生成测试报告的解决方法 #################
    右键运行脚本时，显示的是unittest in xxx；
    Edit configurations...下，将脚本从Python tests下删除，在Python下新建脚本即可；
    '''
