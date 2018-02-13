#coding:utf-8
'''
从xml中读取数据
学习资料链接：http://www.cnblogs.com/fnng/p/3581433.html#undefined
'''

from xml.dom import minidom     #从xml/dom文件夹下导入minidom.py文件,用来处理XML文件

###########获取标签属性
def dateOne():
    #打开xml文档
    #dom = minidom.parse('D:\Documents\workspace\studySE\Date\dateONE.xml')
    dom = minidom.parse('dateONE.xml')      #parse()用于打开一个XML文件

    #得到文档元素对象
    root = dom.documentElement   #得到dom文档对象元素，并把获得的对象给root  得到xml文件的唯一根元素
    print root.nodeName
    print root.nodeValue
    print root.nodeType
    print root.ELEMENT_NODE

############获得子标签，eg:已知标签<category>的子标签以及标签名字
def dateTwo():
    #打开xml文档
    dom = minidom.parse('dateTwo.xml')
    #得到文档元素对象
    root = dom.documentElement

    #知道元素名字的子元素，可以使用getElementsByTagName方法获取：
    bb = root.getElementsByTagName('maxid')
    b = bb[0]
    print b.nodeName

    cc = root.getElementsByTagName('login')
    c = cc[0]
    print c.nodeName

########################如何区分相同标签名字的标签
def dateThree():
    dom = minidom.parse('dateTwo.xml')
    root = dom.documentElement

    bb = root.getElementsByTagName('caption')
    #获取第3个caption标签名字，索引从0开始
    b = bb[2]
    print b.nodeName

##################获取标签属性,login和item标签都有属性，获取他们的属性
#getAttribute方法可以获得元素的属性所对应的值
def dateFour():
    dom = minidom.parse('dateTwo.xml')
    root = dom.documentElement

    itemlists = root.getElementsByTagName('login')
    item = itemlists[0]
    #查看login的name和value
    print item.nodeName
    print item.nodeValue

    #获取login标签下username和password的值
    un = item.getAttribute('username')
    ps = item.getAttribute('passwd')
    print un, ps

    #获取item标签下id的值，注意有两个id
    tems = root.getElementsByTagName('item')
    #获取第一个item标签中，id的值
    tem = tems[0]
    oneId = tem.getAttribute('id')
    print oneId
    # 获取第二个item标签中，id的值
    tem = tems[1]
    twoId = tem.getAttribute('id')
    print twoId

####################获取标签对之间的数据，获取caption标签对之间的数据

def dateFive():
    dom = minidom.parse('dateTwo.xml')
    root = dom.documentElement

    #第一种方法：#firstChild 属性返回被选节点的第一个子节点，获取该节点人数据.nodeValue
    b = root.getElementsByTagName('caption')
    bb = b[0]
    bbb = bb.firstChild
    print bbb.nodeValue

'''
    #第二种方法：方法二的作用不在于此，它核心功能是可以遍历某一级标签下的所有子标签。
    #########第二种方法目前有bug，运行报错“AttributeError: Element instance has no attribute 'findall'”
    p = root.findall('./login/item')

    for oneper in p:
        for child in oneper.getchildren():
            print child.tag, ':', child.text

    p = root.findall('./item')

    for oneper in p:
        for child in oneper.getchildren():
            print child.tag, ':', child.text
'''

if __name__ == '__main__':
    #dateOne()
    #dateTwo()
    dateThree()
    #dateFour()
    #dateFive()