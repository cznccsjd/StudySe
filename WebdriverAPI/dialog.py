#coding:utf-8
'''
对话框处理
本节重点：
    打开对话框
    关闭对话框
    操作对话框中的元素
    current_window_handle   获得当前窗口
    window_handles  获得所有窗口
'''
import os

import time
from selenium import webdriver

dr = webdriver.Firefox()
filepath = 'file:///' + os.path.abspath('modal.html')
###############div对话框的处理
def dialog():
    dr.get(filepath)
    dr.implicitly_wait(5)
    #打开对话框
    dr.find_element_by_id('show_modal').click()
    time.sleep(2)

    #定位click me 链接，点击
    #dr.find_element_by_id('click').click()
    #用js来定位click me链接并点击
    '''
    下面两句,压根就看不懂什么意思
    '''
    link = dr.find_element_by_class_name('modal-body').find_element_by_id('click')
    dr.execute_script('$(arguments[0]).click()',link)

    time.sleep(2)
    dr.quit()

#一般对话框的处理
#有些弹出对话框窗，通过判断是否为当前窗口的方式进行操作
def other():
    #获取当前窗口
    nowhandle = dr.current_window_handle

    #打开弹窗
    dr.find_element_by_name('xxx').click()

    #获取所有的窗口
    allhandles = dr.window_handles

    for handle in allhandles:
        if handle != nowhandle: #比较当前窗口是不是原先的窗口
            dr.switch_to_window(handle) #获得当前窗口的句柄
            dr.find_element_by_class_name("xxx").click()    #在当前窗口操作
        #回到原先的窗口
        dr.switch_to_window(nowhandle)

if __name__ == '__main__':
    dialog()