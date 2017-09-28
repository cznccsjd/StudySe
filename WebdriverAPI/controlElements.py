#coding:utf-8
'''
定位一组元素
webdriver可以很方便的使用findElement方法来定位某个特定的对象，不过有时需要定位一组对象，
这种情况使用findELements方法；

定位一组对象使用的场景：
1、批量操作对象，比如将页面上所有的checkbox都勾上；
2、先获取一组对象，再在这组对象中过滤出需要具体定位的一些对象，
比如定位出页面上所有的checkbox，然后选择最后一个；
'''

from selenium import webdriver
import time
import os

dr = webdriver.Firefox()
filePath = 'file:///' + os.path.abspath('checkbox.html')

####################定位复选框,勾选所有符合要求的复选框
def checkBox():
    dr.get(filePath)
    #选择页面上所有的input，然后从中过滤出所有的checkbox并勾选
    inputs = dr.find_elements_by_tag_name("input")
    for input in inputs:
        if input.get_attribute('type') == 'checkbox':
            input.click()
    time.sleep(2)
    dr.quit()

############### 去掉最后一个勾选复选框
def checkBoxWithoutLast():
    dr.get(filePath)
    #选择页面上所有的checkbox并勾选
    inputs = dr.find_elements_by_tag_name('input')
    for input in inputs:
        if input.get_attribute('Type') == 'checkbox':
            input.click()

    #去掉最后一个勾选，其实就是再次点击最后一个，用pop()找到最后一个
    dr.find_elements_by_css_selector('input[type=checkbox]').pop().click()

    time.sleep(2)
    dr.quit()


if __name__ == '__main__':
    #checkBox()
    checkBoxWithoutLast()