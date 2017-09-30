#coding:utf-8
'''
testSuite.py所需要的文件
'''

from selenium import webdriver
import time
import unittest

class youdao(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.youdao.com")
        self.driver.implicitly_wait(10)
        self.verificationErrors = []
        self.accept_next_alert = True
        #print "this is youdao setUp;"

    def test_search(self):
        u"""有道搜索测试用例"""
        self.driver.find_element_by_id("translateContent").clear()
        self.driver.find_element_by_id("translateContent").send_keys("selenium")
        self.driver.find_element_by_id("translateContent").submit()
        time.sleep(3)
        #print "this is youdao testcase1;"

    def test_words(self):
        u"""打开有道单词测试用例"""
        self.driver.find_element_by_link_text("背单词").click()
        self.driver.implicitly_wait(10)
        #print "this is youdao testcase2;"

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        #print "this is youdao teardown;"

if __name__ == '__main__':
    unittest.main()
