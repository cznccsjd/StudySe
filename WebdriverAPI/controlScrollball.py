#coding:utf-8
'''
控制浏览器滚动条
有时候我们需要控制页面滚动条上的滚动条，但滚动条并非页面上的元素，这个时
候就需要借助js 是来进行操作。一般用到操作滚动条的会两个场景：
 注册时的法律条文需要阅读，判断用户是否阅读的标准是：滚动条是否拉到最
下方。
 要操作的页面元素不在吸视范围，无法进行操作，需要拖动滚动条

用于标识滚动条位置的代码
<body onload= "document.body.scrollTop=0 ">
<body onload= "document.body.scrollTop=100000 ">
如果滚动条在最上方的话，scrollTop=0 ，那么要想使用滚动条在最可下方，可以
scrollTop=100000 ，这样就可以使滚动条在最下方。
'''
import time

'''
场景一：
先来解决场第一个问题，法律条款是一个内嵌窗口，通过firebug 工具可以定位到内嵌
入窗口可以定位到元素的id ，可以通过下面的代码实现。
js="var q=document.getElementById('id').scrollTop=10000"
driver.execute_script(js)
'''


##############场景二：
#有滚动条的页面到处可见，这个就比较容易找例子，我们以操作百度搜索结果页为例：
from selenium import webdriver

dr = webdriver.Firefox()
dr.get('http://www.baidu.com')
dr.implicitly_wait(5)

dr.find_element_by_id('kw').send_keys('baidu')
dr.find_element_by_id('su').click()
time.sleep(2)

#拖动页面滚动条，将页面拉到最底处
js_bottom = "var q = document.documentElement.scrollTop=10000"
dr.execute_script(js_bottom)
time.sleep(2)

#拖动页面滚动条，将页面拉到最顶处
js_top = "var q = document.documentElement.scrollTop=0"
dr.execute_script(js_top)

time.sleep(2)
dr.quit()

