#!/usr/bin/env python
# coding=utf-8
#声明一个字符串
x = "There are %d type of people." % 10
binary = "binary"
do_not = "don't"
#根据上面的变量声明声明一个字符串
y = "Those who know % s and those who %s." % (binary,do_not) #No.1

print x
print y
#分别打印 x y
print "I said: %r." % x #No.2
print "I also said:'%s'." % y #No.3

hilarious = False
#声明一个格式字符串
joke_evaluation = "Isn't that joke so funny?! %r" #No.4

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side"

print w + e

