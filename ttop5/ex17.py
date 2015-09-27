#!/usr/bin/env python
# coding=utf-8

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copy file from %s to %s." % (from_file, to_file)

# We could do these two on line too, how?
input = open(from_file)
indata = input.read()

print "The input file is %d bytes long." % len(indata)

print "Does the output file exit? %r." % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."

raw_input()

output = open(to_file, 'w')
output.write(indata)

print "Alright, all done!"

output.close()
input.close()
