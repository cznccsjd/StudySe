#coding:utf-8
"""
读取csv文件
首先导入cvs模块，通过reader()方法读取cvs文件；
然后通过for循环便利文件中的每一行数据
"""

#导入csv包
import csv

#读取本地csv文件
date = csv.reader(open('info.csv','r'))

#循环输出每一行信息
for user in date:
    #print user
    """
    打印的结果，每一行数据都是以数组的形式存储的，如果想获取每一列数据，指定数组下表即可
    """
    print u"第二列数据：", user[2]

