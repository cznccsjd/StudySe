#coding:utf-8
'''
调用js方法：execute_script(script,*args)
在当前窗口/框架 同步执行javaScript

script:JavaScript的执行
*args:适用任何JavaScript脚本
使用：
driver.execute_script('document.title')
'''

from selenium import webdriver
import os, time

dr = webdriver.Firefox()
filepath = 'file:///' + os.path.abspath('js.html')

#通过js隐藏元素
'''
执行js一般有两种场景：
    一种是在页面上直接执行JS
    另一种是在某个已经定位的元素上执行
'''

def button():
    dr.get(filepath)
    dr.implicitly_wait(5)
    #####通过js隐藏选中的元素###########第一种方法
    dr.execute_script('$("#tooltip").fadeOut()')
    time.sleep(2)

    time.sleep(2)
    dr.quit()

if __name__ == '__main__':
    button()