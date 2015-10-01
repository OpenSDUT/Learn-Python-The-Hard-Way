from sys import argv
from os.path import exists

script,from_file,to_file=argv

print "Copy from %s to %s."%(from_file,to_file)

input=open(from_file)
indata=input.read()

print "The input file is %d bytes long"%len(indata)

print "Does the outputfile is exist? %r"%exists(to_file)
print "Ready,hit enter to continue."
raw_input()

output=open(to_file,'w')
output.write(indata)

print "Alright all done."

output.close()
input.close()

























