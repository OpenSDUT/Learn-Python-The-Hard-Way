from sys import argv

script , filename = argv

txt = open(filename)

print "This is your txt file %r:" % filename
print txt.read()

xxx = raw_input('> ')
yyy = open(xxx)

print yyy.read()
yyy.close()
