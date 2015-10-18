from sys import argv

script , filename = argv

print "We're going to erase %r." % filename
print "If you don't want that,hit ctrl-c."
print "If you want that , hit return."

raw_input("?")

print "Openning the file..."
xxx = open(filename,'w')

print "Truncating the file.  Goodbye!"
xxx.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "Now I will write these to the file. "

xxx.write(line1)
xxx.write("\n")
xxx.write(line2)
xxx.write("\n")
xxx.write(line3)
xxx.write("\n")
xxx.close()
print ">>>>>>End<<<<<<"

aaa=raw_input("Please hit filename that you want to read.>> ")
yyy=open(aaa)
print yyy.read()
yyy.close()
