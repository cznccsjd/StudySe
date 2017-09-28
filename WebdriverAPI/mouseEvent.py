#coding:utf-8
'''
鼠标事件
WebDriver中，鼠标操作的方法封装在ActionChains类中
ActionChains类提供鼠标操作的常用方法：
perform():  执行所有ActionChains中存储的行为
context_click():    右击
double_click(): 双击
drag_and_drop():    拖动
move_to_element()：  鼠标悬停
'''

from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

dr = webdriver.Firefox()

####################鼠标右击操作
def rightClick():
    dr.get("https://www.baidu.com")
    time.sleep(1)
    login = dr.find_element_by_link_text('登录')
    ActionChains(dr).context_click(login).perform()

    time.sleep(2)
    dr.quit()

def doubleClick():
    #找不到合适的双击操作的页面，先记录使用方法
    ActionChains(dr).double_click(login).perform()  #login是需要进行双击操作的元素

def drapAndDrop():
    #到不到合适的操作页面，先记录使用方法
    #定位元素原有位置
    source = dr.find_element_by_id("111")
    #定位元素将要移动到的目标位置
    target = dr.find_element_by_id('222')
    #执行元素的移动操作
    ActionChains(dr).drag_and_drop(source, target).perform()

#鼠标悬停，打开百度首页-设置-搜索设置
def setting():
    dr.get('http://www.baidu.com')
    dr.implicitly_wait(5)

    #鼠标悬停到设置上
    element = dr.find_element_by_link_text(u'设置')
    ActionChains(dr).move_to_element(element).perform()
    time.sleep(2)
    dr.find_element_by_link_text(u'搜索设置').click()
    time.sleep(2)
    dr.quit()

if __name__ == "__main__":
    #rightClick()
    setting()

