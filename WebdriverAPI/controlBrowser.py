#coding:utf-8
'''
控制浏览器
'''
from selenium import webdriver
import time

dr = webdriver.Firefox()

###############控制浏览器窗口大小####################
def control():
    dr.get("https://www.baidu.com")
    dr.implicitly_wait(5)
    #参数数字为像素点
    print "设置浏览器宽480、高600显示"
    dr.set_window_size(480,600)
    time.sleep(2)
    dr.maximize_window()    #最大尺寸显示
    time.sleep(1)
    dr.quit()

################控制浏览器后退、前进######################
def backForward():
    #访问百度首页
    first_url = 'https://www.baidu.com'
    dr.implicitly_wait(5)
    print "Now access %s" %(first_url)
    dr.get(first_url)

    #访问新闻页面
    second_url = 'https://news.baidu.com'
    dr.implicitly_wait(5)
    time.sleep(2)
    print "Now access %s" %(second_url)
    dr.get(second_url)

    #返回（后退）到百度首页
    print "Back to %s" %(first_url)
    dr.back()
    time.sleep(1)

    #前进到新闻页
    print "Forward to %s" %(second_url)
    dr.forward()
    time.sleep(1)
    dr.quit()

##############模拟浏览器刷新########################
def refresh():
    time.sleep(1)
    dr.refresh()


if __name__ == '__main__':
    #control()
    backForward()