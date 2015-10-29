# -*-coding:utf-8 -*-
#测试strip()函数实现的效果
from urllib import urlopen
str = "000this is a string\texample,let's look if carefuly!0000"
print "注意:只有两端的才有效果,中间的制表符是没有效果的"
print str.strip('0')
print str.lstrip('0')
print str.rstrip('0')
#上面是三种基本形式,还有特殊情况
a = '      123'
b = '\tabcd\t'
print a.strip()
print b.strip()
print "这里的rm删除序列是只要边（开头或结尾）上的字符在删除序列内，就删除掉."
c = "123abc"
print c.strip('21')
print c.strip('12')

#urlopen方法
#WORD_URL = "http://learncodethehardway.org/words.txt"
#WORDS = []
#for word in urlopen(WORD_URL).readlines():
#    WORDS.append(word.strip())

#print urlopen(WORD_URL).info()
#print urlopen(WORD_URL).getcode()
#print urlopen(WORD_URL).geturl()

#capitalize()方法

str = "this is a String!"
print "str.capitalize():", str.capitalize()
a = 'wORD'
print "a.capitalize():",a.capitalize()

#count()方法
str = "this is a string example"
sub = 'exa'
print "str.count('is',0,len(str)):",str.count('is',0,len(str))
print "str.count('s'):",str.count('s')
print "str.count(sub):",str.count(sub)

#replace()方法
str = "this is string example....wow!!! this is really string";
print str.replace("is", "was");
print str.replace("is", "was", 3);
