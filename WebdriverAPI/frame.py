#coding:utf-8
'''
多层框架/窗口定位
switch_to_frame
switch_to_window
对于一个现代的web应用，经常会出现框架（frame）和窗口（window）的应用；
有时候定位一个元素，定位器没有问题，但是一直定位不了，这时候就要检查这个元素是否在一个frame中，
selenium 提供了一个switch_to_frame方法
'''

from selenium import webdriver
import time
import os

dr = webdriver.Firefox()
filePath = 'file:///' + os.path.abspath('frame.html')

##############多层框架定位
def frame():
    dr.get(filePath)
    dr.implicitly_wait(10)  #可能需要手动暂停浏览器的刷新动作

    #定位到iframe f1
    dr.switch_to_frame('f1')
    #定位到iframe f2
    dr.switch_to_frame('f2')
    #定位输入框
    dr.find_element_by_id('kw').send_keys('I have find the iframe')
    time.sleep(2)
    dr.quit()

########### 如果嵌套的是window，就用switch_to_window

if __name__ == '__main__':
    frame()