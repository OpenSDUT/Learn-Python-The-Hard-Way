#!/usr/bin/env python
# coding=utf-8

l = 0
numbers = []

while l < 6:
    print "At the top l is %d" % l
    numbers.append(l)

    l = l + 1
    print "Numbers now:", numbers
    print "At the bottom l is %d" % l

print "The numbers:"

for num in numbers:
    print num
