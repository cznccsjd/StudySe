#coding:utf-8
'''
简单元素操作
'''

from selenium import webdriver
import time

dr = webdriver.Firefox()
dr.get("https://www.baidu.com")

#获得输入框的尺寸
size = dr.find_element_by_id('kw').size
print size

#返回百度页面底部备案信息
text = dr.find_element_by_id('cp').text
print text

#返回元素的属性值，可以是id、name、type或其他任意属性
attribute = dr.find_element_by_id('kw').get_attribute('type')
print attribute

#返回元素的结果是否可见，返回结果为True或者False
result = dr.find_element_by_id('kw').is_displayed()
print result

time.sleep(20)