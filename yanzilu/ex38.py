# -*- coding:utf-8 -*-
#Exercise 38:Doing Things To Lists

ten_things = "Apples Oranges Crows Telephone Light Suger"

print "Wait there's not 10 things in that list,let's fix that."

#将ten_things字符串按照空格进行拆分,并赋值给stuff.
stuff = ten_things.split(' ')

more_stuff = ["Day","Night","Song","Frisbee","Corn","Banana","Girl","boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "Adding :",next_one
	stuff.append(next_one)
	print "There's %d items now." % len(stuff)

#每一次执行pop操作,都会在列表末尾拿出一个元素,然后将该元素删除
print "Now more_stuff is ",more_stuff
print "There we go ",stuff

print "Let's do somethings with stuff."

#打印下标为1的元素
print stuff[1]

#打印倒数第一个元素
print stuff[-1]

#拿出最后一个元素并删除之
print stuff.pop()

#以空格间隔元素打印stuff列表
print ' '.join(stuff)

#以#间隔元素打印stuff列表中的第3到5个元素,且包含第三个不包含第五个,和range[3,5]一样情况
print '#'.join(stuff[3:5])
#print join('#',stuff[3:7])
