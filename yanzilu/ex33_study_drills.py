# -*- coding: utf-8 -*-

#Study drill 1:

numbers = []

def app (i):
	x = 0
	while x < i:
		print"At the top is %d" %x
		numbers.append(x)

		x += 1
		print "Numbers now:",numbers
		print "At the bottom x is %d" %x



print "请输入最大循环次数:"
i =int(raw_input())
app(i)
print "The numbers:"
print numbers


#Study drill 3:

numbers = []

def app (i,j):
	x = 0
	while x < i:
		print"At the top is %d" %x
		numbers.append(x)

		x += j
		print "Numbers now:",numbers
		print "At the bottom x is %d" %x



print "请输入最大循环次数:"
i =int(raw_input())
print "请输入公差"
j = int(raw_input())
app(i,j)
print "The numbers:"
print numbers


#Study drill 5:


def app (i):
	
	print "The i is %d" %i
	#此处的numbers是重新建立的list,属于局部变量,
	#如果不返回,使无法对全局变量numbers产生作用的
	numbers = range(1,i)
	print "The numbers:",numbers


print "请输入最大循环次数:"
i =int(raw_input())
app(i)


#Study drill 5-1:



def app (i):
	numbers = []
	print "The i is %d" %i
	numbers = range(1,i)
	print "The numbers:",numbers
	return numbers



print "请输入最大循环次数:"
i =int(raw_input())
numbers = app(i)
print "The numbers:",numbers
for x in numbers:
	print x







