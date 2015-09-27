#!/usr/bin/env python
# coding=utf-8

from sys import argv

script, input_file = argv


def print_all(f):
    print f.read()


def rewind(f):
    f.seek(0)
# f.seek(0)是重新定位在文件的第0位及开始位置
# file.seek(3)是定位到第3个
# 重新定位到0的好处是不用再次打开文件。


def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "Now let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print three lines."
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
