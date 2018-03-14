#coding:utf-8
"""
从DB中读取数据、写入数据   （需要下载安装MySQLdb模块）

connect对象方法：
close()：关闭数据库连接,注意一旦执行了close()方法，再试图连接对象的方法将会导致异常；
commit():提交当前事务
rollback():取消当前事务
cursor():使用这个连接创建并返回一个游标或类游标的对象
errorhandler(cxn,cur,errcls,errval):作为已给游标的句柄
"""
import MySQLdb
import os
from random import randrange as rrange

def testOne():
    """
    testOne仅仅只是练习书本上的例子，没有特殊作用
    例子内容：Connection后，drop删除某个不存在的库，python执行后报错
    注意：删除的数据库一定要是不存在的，小心玩火自焚！！！！
    :return: 
    """
    conTalk = MySQLdb.Connection(host='172.16.0.20',user='root',passwd='123456',port=3306,charset='utf8')
    conPrivate = MySQLdb.connect(host='172.16.0.118',user='root',passwd='123456',port=3306,charset='utf8')
    print conPrivate, conTalk
    print "上面两种方法都可以使用"
    #conPrivate.query('DROP DATABASE testONE')

def testTwo():
    """
    针对testONE进行改进，使用cursor游标对象和它们的execute()方法；
    例子内容：1、新建库；2、新建表；3、表中插入数据；4、查询数据；5、打印查询结果
    6、更新；7、删除
    :return: 
    """
    conn = MySQLdb.connect(host='172.16.0.118',user='root',passwd='123456',port=3306,charset='utf8',db='testjlz')
    cur = conn.cursor()
    #print cur
    #cur.execute('CREATE DATABASE testjlz')     #新建数据库testjlz,注意connect参数需要删除参数（不能添加）db='testjlz'
    #cur.execute('CREATE TABLE student(name varchar(10),age int(4), sex varchar(8))')       #在testjlz库中，新建表student,注意connect参数需要添加db='testjlz'
    cur.execute("INSERT INTO student values ('zhangsan', 20, 'man')")
    cur.execute("INSERT INTO student values('lisi',19,'man')")
    cur.execute("INSERT INTO student values('hanmeimei', 25, 'woman')")
    cur.execute("SELECT * FROM student where age >= 20")

    for date in cur.fetchall(): #cur.fetchall() 获取所有的记录
        print date

    #更新
    cur.execute("UPDATE student SET name = 'zhangsanyi' where name = 'zhangsan'")
    #删除
    cur.execute("DELETE FROM student where name = 'zhangsanyi'")

    #查询
    result1 = cur.execute("SELECT * from student")
    print result1
    #获取查询的所有记录
    result =cur.fetchall()
    #打印查询的结果
    print result

"""
def testThree():
    '''
    数据库接口程序应用程序举例，p605末尾
    
    :return: 
    '''
    COLSIZ = 10
    RDBMSs = {'s': 'sqlite', 'm':'mysql', 'g':'gadfly'}
    DB_EXC = None

    def setup():
        return RDBMSs[raw_input('''
        Choose a database system:
        
        (M)ySQL
        (G)adfly
        (S)QLite
        
        Enter choice:''').strip().lower()[0]]
    def connect(db, dbName):
        global DB_EXC
        dbDir = '%s_%s' % (db, dbName)

        if db == 'sqlite':
            try:
                import sqlite3
            except ImportError, e:
                #try:
                    #from pysqlite2 import dbapi2 as sqlite3 #需要找到pysqlite2,但是python2.7自带的是sqlite3，所以用不到
                print "sqlite3没有找到~"

                DB_EXC = sqlite3
                if not os.path.lsdir(dbDir):
                    os.mkdir(dbDir)
                cxn = sqlite3.connect(os.path.join(dbDir,dbName))

        elif db == 'mysql':
            try:
                import MySQLdb
                import _mysql_exceptions as DB_EXC
            except ImportError, e:
                return None

            try:
                cxn = MySQLdb.connect(db=dbName)
            except DB_EXC.OperationalError, e:
            cxn = MySQLdb.connect(user='root')  #疑问：为啥cxn不用空几行，作为except
            try:
                cxn.query('DROP DATABASE %s' % dbName)
            except DB_EXC.OperationalError, e:
                pass
            cxn.query('CREATE DATEBASE %s' % dbName)
            cxn.query("GRANT ALL ON %s.* to ''@'localhost'" % dbName)
            cxn.commit()
            cxn.close()
            cxn = MySQLdb.connect(db=dbName)
        elif db == 'gadfly':
            print "没有gadfly文件，需要再下载，目前用不到，本例就不用这个文件了"

    def create(cur):
        try:
            cur.execute('''
            CREATE TABLE user (
                login VARCHAR(8),
                uid INTEGER,
                prid INTEGER)
            ''')
        except DB_EXC.OperationalError, e:
            drop(cur)
            create(cur)
        drop = lambda cur:cur.execute('DROP TABLE users')
        NAMES = (
            ('aaron',8312),
        )
"""





if __name__ == '__main__':
    testOne()
    #testTwo()