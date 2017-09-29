#coding:utf-8
from selenium import webdriver
import os, time

file = open("./date.txt","r")   #open()方法以只读方式（r）打开本地的date.txt文件
values = file.readlines()   #readlines()方法逐行读取文件内容
file.close()
#print values

for search in values:
    browser = webdriver.Firefox()
    browser.get("http://www.baidu.com")
    browser.implicitly_wait(5)
    browser.find_element_by_id("kw").send_keys(search)
    browser.find_element_by_id("su").click()
    time.sleep(2)
    browser.quit()