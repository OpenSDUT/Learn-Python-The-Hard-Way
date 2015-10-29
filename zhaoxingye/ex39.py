ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list,let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day","Night","Song","Frisbee","Corn","Banana","Girl","Boy"]

while len(stuff) !=10:
    next_one = more_stuff.pop()
    print "Adding: ",next_one
    stuff.append(next_one)
    print "There's %d items now." % len(stuff)

print "There we go: ",stuff

print "Let's do some things with stuff."

#print stuff[1]
#print stuff[0]
#print stuff[-1]
#print stuff[-2]
#print stuff[-3]
#print stuff[-4]
#print stuff[-5]
#print stuff.pop()
print ' '.join(stuff)
print '*'.join(stuff[0:2])
# join lianjie
#for i in stuff:
#    print "%r" % i





