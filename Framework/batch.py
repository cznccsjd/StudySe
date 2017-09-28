#coding:utf-8
'''
批量执行测试集
将多个自动化用例，一起执行
'''

from selenium import webdriver
import unittest, time

class Baidu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.base_url = "http://www.baidu.com"
        self.verificationErrors = []
        self.accept_next_alert = True

    #百度搜索用例
    def test_baidu_search(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        time.sleep(1)
        driver.find_element_by_id("kw").send_keys("selenium webdriver")
        time.sleep(1)
        driver.find_element_by_id("su").click()
        time.sleep(2)
        driver.close()

    #百度设置用例
    def test_baidu_set(self):
        driver = self.driver
        #进入搜索设置页
        driver.get(self.base_url + "/gaoji/preferences.html")
        time.sleep(2)

        #设置每页搜索结果为50条
        m = driver.find_element_by_name("NR")
        m.find_element_by_xpath("//option[@value='50']").click()
        time.sleep(2)

        #保存设置的信息
        driver.find_element_by_xpath("//input[@value='保存设置']").click()
        time.sleep(2)
        driver.switch_to_alert().accept()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

'''
虽然已经实例了多个用例一起跑，但这样仍然不合理，几个用例一起执行还好，如果几十个，几百个
用例的话，这个文件将会变得无比庞大，不利于维护。
所以合理的做法是一个用例一个文件，把所有文件放到一个文件夹下，通过单独的脚本控制所有用例的执行，
将脚本的执行结果输出到一个log文件中。
eg：
import os
#列出某个文件夹下所有的case，这里用的是Python，所在py文件运行一次后会生成一个pyc的副本
caselist = os.listdir(' D:\\selenium_use_case\\test_case')       #filepath = D:\\selenium_use_case\\test_case
for a in caselist:
    s = a.split('.')[1:][0] #选取索要执行的用例
    if s == 'py'
        #此处执行dos命令并将结果保存到log.txt
        os.system('D:\\selenium_use_case\\test_case\\%s 1>>log.txt 2>&1'%a)
'''