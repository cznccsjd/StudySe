#coding:utf-8
'''
用户名密码参数化
解决循环调用
'''
#### 固定读取用户名、密码
#   创建一个fun.py文件，定义一个字典方法

import fun  #导入fun函数
from selenium import webdriver
import time, os

def readDic():
    #循环调用字典里的用户名、密码，分别赋值给k , v
    for k, v in fun.dic().items():
        driver = webdriver.Firefox()
        driver.get("https://www.xin.com/beijing/")
        driver.implicitly_wait(10)
        driver.find_element_by_id("loginA").click()  # 点击登录
        time.sleep(1)
        driver.find_element_by_id("search").send_keys(k)  # 输入用户名
        time.sleep(1)
        driver.find_element_by_id("psw5").send_keys(v)  # 输入密码
        time.sleep(3)
        driver.quit()

def readFun():
    k, v = fun.user()   #通过调用函数获得用户名&密码
    print k,v

    driver = webdriver.Firefox()
    driver.get("https://www.xin.com/beijing/")
    driver.implicitly_wait(10)
    driver.find_element_by_id("loginA").click()  # 点击登录
    time.sleep(1)
    driver.find_element_by_id("search").send_keys(k)  # 输入用户名
    time.sleep(1)
    driver.find_element_by_id("psw5").send_keys(v)  # 输入密码
    time.sleep(3)
    driver.quit()


if __name__ == '__main__':
    #readDic()
    readFun()