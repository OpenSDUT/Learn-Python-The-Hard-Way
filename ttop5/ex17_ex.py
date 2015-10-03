#!/usr/bin/env python
# coding=utf-8

prompt = "->"

print "from_filename:"
from_file = raw_input(prompt)

x = open(from_file)
data = x.read()

print "to_filename:"
to_file = raw_input(prompt)

y = open(to_file, 'w')
y.write(data)

y.close()
x.close()

print "OK, all done!"
