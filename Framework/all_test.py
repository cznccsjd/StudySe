#coding=utf-8
"""
在testSuite.py中，存在一个问题，用例写多了，不方便管理；本文件将尝试调整结构；
1、
本文件是调用例的程序，不是执行用例的，所以移出来，结构上会更为合理；
建议结构事例：
/selenium_use_case/test_case/unite/test_baidu.py
                            /unite/test_youdao.py
                            /unite/__init__.py
                            /unite/...
                            /all_tests.py
在上面的目录结构中，unite文件夹下存放具体的执行用例，all_tests.py应与unite文件夹平级；
此外，需要在unite文件夹下放一个__init__.py文件，文件内容可以为空；
直接移出来后再运行all_tests.py文件，会提示找不到测试文件，所以我们要对代码做调整，把文件夹加到sys.path下就可以找到了；
在all_tests.py头部添加一下内容：
import sys
sys.path.append("/selenium_use_case/test_case")
from unite import test_baidu
from unite import test_youdao
...

2、__init__.py文件解析
all_tests.py移出来了，但还存在问题，导入包（用例文件）也是个问题，假如几个用例可以通过“from unite import test_xxx”的方式导入，
那上百条用例导入显然很不方便；此时可以使用__init__.py文件；
2.1 python执行import语句时的操作：
    第1步，创建一个新的，空的module对象（它可能包含多个module）；
    第2步，把这个module对象插入sys.module中；
    第3步，装载module的代码（如果需要，首先必须编译）
    第4步，执行新的module中对应的代码；
    在执行第3步时，首先要找到module程序所在的位置，搜索的顺序时：
        当前路径（以及从当前目录指定的sys.path），然后是PYTHONPATH，然后是python的安装设置相关的默认路径。
        正因为存在这样的顺序，如果当前路径或PYTHONPATH中存在与标准module同样的module，则会覆盖标准module，也就是说，如果当前目录下存在xml.py，那么
        执行import xml时，导入的是当前目录下的module，而不是系统标准的xml；
        了解了这些，我们就可以先构建一个package，以普通module的方式导入，就可以直接访问此package中的各个module了。python中的package必须包含一个__init__.py文件；
其实__init__.py文件中可以有内容，我们在导入一个包时，实际上导入了它的__init__.py文件；在__init__.py文件添加导入包：
import test_baidu
import test_youdao
然后，all_tests.py文件这样修改：
...
import sys
sys.path.append("/selenium_use_ase/test_case")
from unite import *
...
上面，“*”星号表示导入unite目录下所有的文件：在unite目录下创建测试用例文件，只用在__init__.py文件下罗列就可以了，而对于all_tests.py文件来说不需要做任何调整；

3、调用多级目录的用例
当测试用例达到一定量级的时候，为了便于管理，必定需要在目录下面再分目录，假设有如下结构：
/selenium_use_case/test_case/unite/test_baidu.py
                            /unite/test_youdao.py
                            /unite/sougou/test_sougou.py    ---二级测试用例目录
                            /unite/sougou/__init__.py
                            /unite/sougou/...
                            /unite/__init__.py
                            /unite/...
                            /all_tests.py
接着在/unite/__init__.py文件下加入：
from sougou impot *
当然，/unite/sougou/目录下也要加__init__.py文件，并且加入包，掌握这个技巧，再也不用担心多级目录的问题了。

4、改进用例的读取
all_tests.py中，下面代码也有风险：
suite = doctest.DocTestSuite()
suite.addTest(unittest.makeSuite(test_baidu.Baidu))
suite.addTest(unittest.makeSuite(test_youdao.Youdao))
suite.addTest(unittest.makeSuite(test_sougou.Sougou))
改进后的代码，见advanced()  ps:只是原文代码，跟我本文路径不一致，此段代码仅供参考
"""
sys.path.append("./selenium_use_case/test_case")
from selenium import webdriver
import unittest, time
import HTMLTestRunner

#将用例组建成数组
alltestnames = [
    'unite.test_baidu.Baidu',
    'unite.test_youdao.Youdao',
    'unite.sougou.test_sogou.Sougou'    #注意这个用例是二级目录下的
]

suite = unittest.TestSuite()

if __name__ == '__main__':
    #这里我们可以使用defaultTestLoader.loadTestsFromNames(),
    #但如果不提供一个良好的错误消息时，它无法加载测试
    #所以我们加载所有单独的测试，这样将会提高脚本错误的确定
    for test in alltestnames:
        try:
            #最关键的一句，循环执行数据数里的用例
            suite.addTest(unittest.defaultTestLoader.loadTestsFromName(test))
        except Exception:
            print 'Error:Skipping tests from "%s".' % test
            try:
                __import__(test)
            except ImportError:
                print 'Could not import the test module.'
            else:
                print 'Could not load the test suite.'
            from traceback import print_exc
            print_exc()

    print 'Running the tests...'

    filename = 'D:\\result21.html'
    fp = file(filename, 'wb')

    runner = HTMLTestRunner.HTMLTestRunner(stream = fp, title='Report_title',description='Report_description')
    runner.run(suite)

####################################
#   20170930 上面的代码没看明白。。。。。
