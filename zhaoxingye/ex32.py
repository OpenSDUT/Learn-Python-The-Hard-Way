the_count=[1,2,3,4,5,6,7]
fruits=['apples','orange','pears','apricots']
change=[1,'pennies',2,'dimes',3,'quarters']

for number in the_count:
    print "This is count %d" % number
for fruit in fruits:
    print "A fruit of type: %s" % fruit
for i in change:
    print "I got %r" % i

elements=[]
for i in range(0,8):
    print "Adding %d to the list." % i
    elements.append(i)
for i in elements:
    print "Element was : %d" % i

a=[]
for i in fruits:
    a.append(i)
for i in a:
    print "a[%s]= %s" %(i,i)
