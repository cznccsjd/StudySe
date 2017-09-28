#coding:utf-8
'''
cookie处理
本节重点：
driver.get_cookies()    获得cookie信息
add_cookie(cookie_dict)     向cookie添加会话信息
delete_cookie(name) 删除特定（部分）的cookie
delete_all_cookies()    删除所有cookie
'''

from selenium import webdriver
import time

dr = webdriver.Firefox()

###################
#   打印cookie信息
###################
def printCookie():
    dr.get('http://www.baidu.com')
    dr.implicitly_wait(5)
    #获取cookie信息
    cookie = dr.get_cookies()
    print cookie

    time.sleep(2)
    dr.quit()

########################
##  对cookie操作
# 有针对性的打印自己想要的信息
########################
def operateCookie():
    dr.get("http://www.baidu.com")
    dr.implicitly_wait(5)
    #向cookie的name和value添加会话信息
    dr.add_cookie({'name':'jlz','value':'jlz-Value'})
    #print dr.get_cookies()\

    #删除一个特定的cookie
    dr.delete_cookie("PSTM")

    #遍历cookies中的name和value
    #for cookie in dr.get_cookies():
    #    print "%s -> %s" % (cookie['name'], cookie['value'])

    #删除所有的cookies
    dr.delete_all_cookies()
    print dr.get_cookies()

    time.sleep(2)
    dr.quit()

########################
##      博客园登录分析cookie
#       勾选保存保密和不保存密码，cookie值不一致,可以通过下面代码验证
#       下面方法未完成
#########################
def blog():
    #登录博客园
    dr.get("https://passport.cnblogs.com/user/signin?ReturnUrl=https%3A%2F%2Fwww.cnblogs.com%2F")
    dr.implicitly_wait(5)
    #通过用户名、密码登录
    dr.find_element_by_id("input1").send_keys("test")
    dr.find_element_by_id("input2").send_keys("password")


if __name__ == '__main__':
    #printCookie()
    operateCookie()