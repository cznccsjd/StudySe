#coding:utf-8
'''
该文件定义一个字典方法，供其他文件调用:
字典可以方便的存放k,v键值对，一个键对应一个值；
如果密码中有非数字，需要加单引号；
'''

def dic():
    d = {'admin':123456,'root':'qwertyuiop'}
    print "sucess: read username and password!"
    return d

def user(k = 'adminroot',v = 123456):
    print "success: read username and password 11!"
    return k, v