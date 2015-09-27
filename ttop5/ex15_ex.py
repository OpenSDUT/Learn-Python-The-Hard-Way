#!/usr/bin/env python
# coding=utf-8

prompt = "->"

print "Input filename:"
filename = raw_input(prompt)

content = open(filename)

print content.read()

content.close()
