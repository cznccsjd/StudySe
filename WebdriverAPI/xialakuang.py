#coding:utf-8
'''
下拉框处理
重点：处理下拉框；
    switch_to_alert();
    accept();
下拉框一种常见的页面元素，对于一般的元素，只需要一次就定位，但下拉框里面的内容需要进行两次定位；
先定位到下拉框，在定位到下拉框内的选项；
'''
import os
from selenium import webdriver
import time
from selenium.webdriver import ActionChains

dr = webdriver.Firefox()

#通过脚本来选择下拉列表里的$10.69
def xiala():
    file_path = 'file:///' + os.path.abspath('drop_down.html')
    dr.get(file_path)
    time.sleep(2)

    #先定位到下拉框
    box = dr.find_element_by_id('ShippingMethod')
    time.sleep(2)
    #再点击下拉框下的选项
    box.find_element_by_xpath("//option[@value='10.69']").click()
    time.sleep(2)

    dr.quit()

def baiduSetting():
    '''
    百度搜索设置下拉框操作
    有问题，无法定位到“保存设置”按钮
    '''

    dr.get('http://www.baidu.com')
    dr.implicitly_wait(5)

    # 进入搜索设置页面
    element = dr.find_element_by_link_text('设置')
    ActionChains(dr).move_to_element(element).perform()
    time.sleep(2)
    dr.find_element_by_link_text('搜索设置').click()

    # 设置搜索结果，每页显示50条
    dr.find_element_by_name('NR')
    dr.find_element_by_xpath("//option[@value='20']").click()
    time.sleep(1)
    # 点击保存
    dr.find_element_by_xpath("//*[@id='gxszButton']/a[1]").click()
    time.sleep(2)
    # 跳转到toast弹窗
    dr.switch_to_alert().accept()   #接收弹窗


if __name__ == '__main__':
    #xiala()
    baiduSetting()