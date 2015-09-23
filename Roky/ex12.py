#coding:utf-8

#这句话会用 “Name?” 提示用户，然后将用户输入的结果赋值给变量 y.
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)
