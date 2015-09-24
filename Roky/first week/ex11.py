#coding:utf-8

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

#单引号需要被转义，从而防止它被识别为字符串的结尾。
print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)
