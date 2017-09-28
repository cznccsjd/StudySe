#coding:utf-8
'''
本节重点：
text 返回alert/confirm/prompt的文字信息
accept 点击确认按钮
dismiss 点击取消按钮，如果有的话
send_keys 输入值，这个alert\confirm没有对话框就不能用，不然报错
'''

#用法举例：

#接受警告信息
alert = driver.switch_to_alert()
alert.accept()

#得到文本信息打印
alert = driver.switch_to_alert()
print alert.text()

#取消对话框（如果有的话）
alert = driver.switch_to_alert()
alert.dismiss()

#输入值
alert = driver.switch_to_alert()
alert.send_keys("xxx")
