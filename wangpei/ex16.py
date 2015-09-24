#!/usr/bin/env python
# coding=utf-8
from sys import argv

script,filename = argv
print("we're going to erase %r"%filename)
print("if you don't want that,hit CTRL-C(^C)")
print("if you do want that,hit RETURN")

input("?")

print("OPening the file...")
target = open(filename,"w")

print("Truncating the file.Goodbye")
target.truncate()

print("Now I'm going to ask you for three lines")

line1 = input("line1:")
line2 = input("line2:")
line3 = input("line3:")

print("I'm going to write these to the file")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally,we close it")
target.close()
