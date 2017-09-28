#coding:utf-8
'''
层级定位
页面上有很多个属性基本相同的元素，现在需要具体定位到其中一个，
由于属性基本相当，所以在定位的时候会有些麻烦，这时候就需要
用到层级定位，限定为父元素，然后再通过父元素定位子孙元素；
'''

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import time
import os


dr = webdriver.Firefox()

filePath = 'file:///' + os.path.abspath('level_locate.html')
dr.get(filePath)

#找到Link1链接，弹出下拉列表
#有个坑，先定位到下拉框（是这个下拉框），等下拉框出现后，再定位下拉框上的具体元素（eg:Action）
dr.find_element_by_link_text('Link1').click()
WebDriverWait(dr, 10).until(lambda drs : drs.find_element_by_id('dropdown1').is_displayed())
element = dr.find_element_by_id('dropdown1').find_element_by_link_text("Something else here")
#鼠标事件，鼠标右击
ActionChains(dr).context_click(element).perform()
time.sleep(3)
dr.quit()

'''
#自己测试WebDriverWait.until()方法
def one():
    print '这是我一个空方法，用来测试WebDriverWait.until()'

def until():
    WebDriverWait(dr, 5).until(lambda x : x = 5)

if __name__ == '__main__':
    #one()
    #until()
'''