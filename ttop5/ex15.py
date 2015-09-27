#!/usr/bin/env python
# coding=utf-8

from sys import argv

script, filename = argv

txt = open(filename)

print "Here is your file %r:" % filename
print txt.read()

print "Type of the filename again:"
file_again = raw_input("->")

txt_again = open(file_again)

print txt_again.read()
