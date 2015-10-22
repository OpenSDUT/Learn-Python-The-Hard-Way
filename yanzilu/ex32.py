# -*- coding: utf-8 -*-
#Exercise 32:Loops and List
the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','banana']
change = [1,'pennies',2,'dimes',3,'quarters']

print "change[0]: ", change[0]
print "change[2:5]: ", change[2:5] 

#this first kind of for-loop goes through a list
for number in the_count:
	print "This is count %d" %number

#same as above
for fruit in fruits:
	print "A fruit of type:%s"%fruit

#also we can go through mixed lists too
#notice we have to use %r since we don't know what's in it
for i in change:
	print "I got %r"%i

#we can also build lists,first start with an empty one
elements = []

#then use the range function to do 0 to 5 counts
for i in range(0,6):
	print "Adding %d to the list."% i
	#append is a function that lists understand
	elements.append(i)

#now we can print them out too
for i in elements:
	print "Element was : %d" % i



print "the_count[3]:",the_count[3]
the_count[3] = 2015
print "the_count[3]:",the_count[3]
the_count[3] = 'The_count'
print "the_count[3]:",the_count[3]

print the_count
del the_count[3]
print "After deleting value at index 3 : "
print the_count

#计算the_count列表的长度
print len(the_count)
#组合两个列表
list1 = the_count + fruits
print list1
#循环列表元素
list2 = fruits * 3
print list2
#查看某一个元素是否存在于列表中
flag = 7 in the_count
print flag
flag = 'banana' in fruits
print flag
#迭代效果
for x in change:
	print x

#比较两个列表的元素
print "Compare the_count and fruits"
print cmp(the_count,fruits)
print "Compare the_count and the_count"
print cmp(the_count,the_count)
print "Compare fruits and the_count"
print cmp(fruits,the_count)

#返回列表元素最大最小值
print "change max is:",max(change)
print "change min is:",min(change)

#在列表末尾添加新的对象
change.append(2015)
print "new change is:",change

#统计某个元素在列表中出现的次数
print change.count(1)

#在列表末尾一次性追加另一个序列的多个值
print "old change is :",change
change.extend(the_count)
print "new change is :",change

#从列表中找出某个值第一个匹配项的索引位置

print "the first 1 in change is :",change.index(1)

#将对象插入列表
#指在第一个参数的位置插入第二个参数
change.insert(3,'love')
print change


#移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
print change.pop()

#移除列表中某个值的第一个匹配项
change.remove(3)
print change;

#反向列表中元素

change.reverse()
print change;

#对原列表进行排序,默认按照从小到大顺序
change.sort()
print change
