#coding:utf-8
'''
键盘按键
键盘按键用法；
键盘组合键用法；
send_keys()输入中文乱码问题；  -->输入字符前加个u，可以避免乱码问题

##################
要想调用键盘按键操作需要引入keys 包：
from selenium.webdriver.common.keys import Keys
通过send_keys()调用按键：
send_keys(Keys.TAB) # TAB
send_keys(Keys.ENTER) # 回车
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

dr = webdriver.Firefox()

################键盘按键用法
def keyboard():
    dr.get("https://www.baidu.com/")
    dr.implicitly_wait(10)
    dr.maximize_window()

    time.sleep(1)
    dr.find_element_by_link_text('登录').click()
    dr.implicitly_wait(5)
    dr.find_element_by_id('TANGRAM__PSP_10__userName').clear()  #定位用户名
    dr.find_element_by_id('TANGRAM__PSP_10__userName').send_keys("sendkeys")
    time.sleep(2)

    # tab 的定位相相于清除了密码框的默认提示信息，等同上面的clear()
    dr.find_element_by_id('TANGRAM__PSP_10__userName').send_keys(Keys.TAB)  #在用户名输入框通过按TAB键定位到密码输入框
    time.sleep(2)
    dr.find_element_by_id("TANGRAM__PSP_10__passwordLabel").send_keys('123456') #定位密码
    ##通过定位密码框，enter（回车）来代替登陆按钮
    dr.find_element_by_id("TANGRAM__PSP_10__submit").send_keys(Keys.ENTER)
    time.sleep(3)
    dr.quit()


##########################键盘组合键用法
def keyboardKeys():
    dr.get("http://www.baidu.com/")
    dr.implicitly_wait(10)
    dr.maximize_window()

    dr.find_element_by_link_text('登录').click()
    dr.implicitly_wait(5)
    dr.find_element_by_id('TANGRAM__PSP_10__userName').clear()  #定位用户名
    dr.find_element_by_id('TANGRAM__PSP_10__userName').send_keys("sendkeys")
    time.sleep(2)

    #ctrl+a 全选输入的内容
    dr.find_element_by_id('TANGRAM__PSP_10__userName').send_keys(Keys.CONTROL, 'a')
    time.sleep(2)
    #ctrl+x 剪切输入的内容
    dr.find_element_by_id('TANGRAM__PSP_10__userName').send_keys(Keys.CONTROL, 'x')
    time.sleep(2)
    dr.quit()

if __name__ == "__main__":
    #keyboard()
    keyboardKeys()
