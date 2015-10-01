from sys import argv
script,filename=argv

print "We are going to erase %r."%filename
print "If you don't want that,hit CRTL+C"
print "If you do want that ,hit enter."

raw_input('?')

print "opening the file....."

target=open(filename,'w')

print "Truncating the file."
target.truncate()

print "Now you can write three line."
line1=raw_input('line1 :')
line2=raw_input('line2 :')
line3=raw_input('line3 :')

print "We write the three line in the %r."%filename
target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target,write('\n')

print "And finally,we close it."

target.close()






