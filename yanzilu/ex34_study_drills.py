# -*- coding:utf-8 -*-

#study drill 1:

animals = []
def input(m):
	print "一共要输入 %d 只小动物名称" % m
	x = 0
	while x < m:
		print " %d 的位置存放第 %d 个小动物,请输入名称:" %(x,x+1)
		animals.append(raw_input())
		x += 1

m =int (raw_input("请输入小动物的数目:"))
input(m)
print"这些小动物依次为:",animals
