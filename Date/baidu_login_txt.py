#coding:utf-8
"""
下面代码虽然可以从txt文本中读取用户名和密码，但是有着明显的缺点：
1、三用户名密码分别在不同的文件里，这就要求用户名和密码必须一一对应；
2、必须指定读取长度，测试readlines()并不是读取的一行数据；
3、无法循环读取
"""

from selenium import webdriver
import os, time

file1 = open("./date_username.txt","r")  #打开用户名文件
users = file1.read(5)   #读取5位
file1.close()

file2 = open("./date_password.txt", "r")    #打开密码文件
passwords = file2.read(6)   #读取6位
file2.close()

driver = webdriver.Firefox()
driver.get("https://www.xin.com/beijing/")  #打开优信二手车网
driver.implicitly_wait(10)
driver.find_element_by_id("loginA").click() #点击登录
time.sleep(1)
driver.find_element_by_id("search").send_keys(users)    #输入用户名
time.sleep(1)
driver.find_element_by_id("psw5").send_keys(passwords)  #输入密码
time.sleep(3)
driver.quit()
