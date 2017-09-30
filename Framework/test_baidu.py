#coding=utf-8
"""
该文件为testSuite.py调用的文件
"""

from selenium import webdriver
import unittest, time

class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.baidu.com")
        self.driver.implicitly_wait(10)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_search(self):
        u"""百度搜索测试用例"""
        self.driver.find_element_by_id("kw").clear()
        self.driver.find_element_by_id("kw").send_keys("selenium")
        self.driver.find_element_by_id("kw").submit()

    def test_set(self):
        u"""百度设置测试用例"""
        self.driver.find_element_by_link_text("设置").click()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()