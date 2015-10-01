#!/usr/bin/env python
# coding=utf-8

numbers = []


def loop(number, step):
    i = 0
    while i < number:
        print "At the top i is %d" % i
        numbers.append(i)

        i += step
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i


if __name__ == "__main__":
    loop(10, 2)
    for num in numbers:
        print num
