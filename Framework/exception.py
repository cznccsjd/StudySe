#coding:utf-8
'''
异常捕捉与错误截图
我们不需要永运都运行成功的用例，他本身没有什么意义，关键是捕捉到错误，
并把错误截图保存，这是一个很实用的功能，给错误定位带来方便。
'''
from selenium import webdriver
import unittest, os, time

class Baidu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(2)
        self.base_url = "http://www.baidu.com"
        self.verificationErrors = []
        self.accept_next_alert = True

    #百度搜索用例
    def test_baidu_search(self):
        driver = self.driver
        driver.get(self.base_url + "/")

        try:
            #kwddd是一个无法找到的元素id
            driver.find_element_by_id("kwddd").send_keys("selenium webdriver")
        except:
            #如果没有找到上面的元素就截取当前页面
            driver.get_screenshot_as_file("D:\Documents\workspace\studySE\Error_pics\err1808311542002.png")

        driver.find_element_by_id("su").click()
        time.sleep(2)
        driver.close()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)

    if __name__ == "__main__":
        unittest.main()