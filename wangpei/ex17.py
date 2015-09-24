#!/usr/bin/env python
# coding=utf-8
from sys import argv
from os.path import exists

script,from_file,to_file = argv

print("Copying from %s to %s"%(from_file,to_file))

#....
xinput = open(from_file)
indata = xinput.read()

print("The input file is %d bytes long"%len(indata))

print("Does the output file exists %r"%exists(to_file))
print("ready hit return to continue,CTRL-C to abort")
input("please input")

output = open(to_file,"w")
output.write(indata)
print("Alright,all done")

output.close()
xinput.close()
