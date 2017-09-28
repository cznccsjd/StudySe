#coding:utf-8
'''
文件上传
文件上传一般是打开一个本地窗口，从窗口中选择本地文件，因此难点在于如何操作本地窗口添加上传文件
selenium webdriver中，只需要定位到上传按钮，通过send_keys添加本地文件路径即可（绝对路径和相对路径都可以，关键在于文件需要存在）
'''

from selenium import webdriver
import time
import os

dr = webdriver.Firefox()

#上传文件的例子
def test():
    filePath = 'file:///' + os.path.abspath('upload_file.html')
    upload_file = os.path.abspath('upload_file.html')
    print filePath
    dr.get(filePath)

    dr.find_element_by_name('file').send_keys(upload_file)
    time.sleep(3)
    dr.quit()


if __name__ == '__main__':
    test()