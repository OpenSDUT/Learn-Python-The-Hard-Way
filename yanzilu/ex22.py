#What Do You Know So Far?
# -*- coding:utf-8 -*-
print """
1.Python中，print用来打印，"#"用来注释
2.# -*- coding:utf-8 -*-用来输入汉字
3.+ , - , * , / , % , < , <= , > , >= 在Python中正常使用
4.Python中变量名由字母，数字，下划线组成，且数字不能打头
5.Python中自己判断变量类型，无需用户指定
6.打印变量
    (1)可以用","分割字符串和变量名，如：print"There are",cars,"cars available."
    (2)可以用"%"来控制输出，如：print "There are %d cars available." % cars
    (3)如果输出序列中需要用到多个变量，则采用如下形式打印：
        print "If I add %d,%d and %d,I will get %d" % (a,b,c,a+b+c)
    (4)%s,%r,%d,%f等统称为格式控制符，%s用来输出字符串，输出的形式是面向用户看到的形式，
    %r一般用于调试的时候，原数据是什么样子，就会输出什么样子，%d用于输出整数类型。
    (5)当"+"两边连接数字的时候，则进行数学运算,如果两边是字符串，则进行拼接运算，将后面字符串拼接到前面的结尾处。
    (6)如果要打印一行，且不需要换行，但是在代码中一行有很长，则采用","进行连接，如：
        print "This is a line,but it is very long,and we can use ',' to",
        print "content this two lines."
        那么，这两行就回在一行中打印出来。
    (7)如果要按照输入的格式打印出来，则采用将内容放在三个双引号之间的形式，本文的打印就采用了这种方式。
7.Python支持的转义序列有以下几种：
    转义字符            功能
    \\                  反斜杠(\)
    \'                  单引号(')
    \"                  双引号(")
    \a                  ASCII响铃符(BEL)
    \b                  ASCII退格符(BS)
    \f                  ASCII进纸符(FF)
    \n                  ASCII换行符(LF)
    \N(name)            Unicode数据库中的字符名,其中，name是它的名字，仅适用Unicode
    \r                  ASCII回车符(CR)
    \t                  ASCII水平制表符(TAB)
    \uxxxx              值为16位十六进制值xxxx的字符(仅适用Unicode)
    \Uxxxxxxxx          值为32位十六进制值xxxxxxxx的字符(仅适用Unicode)
    \v                  ASCII垂直制表符(VT)
    \ooo                值为八进制值ooo的字符
    \xhh                值为十六进制数hh的字符
8.Python中，通过raw_input()接收用户输入的信息，也可以适用raw_input("")的形式，在双引号中添加提示，如：
    age = raw_input("How old are you?")
9.Python中采用import引入脚本，如：from sys import argv，即引入sys模块，argv是参数变量，保存着运行Python脚本时传递给Python脚本的参数
解包是将argv参数里的信息赋值给多个变量，如:script,first = argv,其中script记录了脚本信息，解包时必不可少。
10.Python中文件的使用
    (1)打开文件：txt = open(filename),默认以只读的方式打开；txt = open(filename,'w')是以写文件的方式打开，文件中原有的内容会被覆盖；
    txt = open(filename,'a')是以追加写文件的方式打开，文件中原有的内容不会丢失；
    txt = open(filename,'w+'),txt = open(filename,'r+'),txt = open(filename,'a+')都是以读写的方式打开文件
    (2)读取文件：txt.read()，会将文件中的内容全部读取出来
    (3)关闭文件：txt.close()
    (4)读取文本文件中的一行：txt.readline()
    (5)清空文件：truncate()
    (6)将stuff写入文件：txt.write(stuff)
    (7)计算文件长度：len(txt)
    (8)判断文件是否存在，首先引入判断方法：from os.path import exists，然后判断：exists(filename),如果存在，则返回True
    (9)回到文件首部：txt.seek(0)
11.Python中，以"def"定义函数，后面紧跟函数名，然后是括号括起来的参数变量，紧跟着括号的是":",如：
def add(a,b):
    c = a + b
    return a,b,c
12.当有多个返回值的时候，使用","分隔，函数名是由字母，数字和下划线组成，函数体通过空格缩进辨别
13.函数可以传递文件，如：
def print_all(f):
    print f.read()
txt = open(filename)
print_all(txt)
"""
