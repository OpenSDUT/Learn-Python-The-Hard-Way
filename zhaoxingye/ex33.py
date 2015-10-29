i = 0
numbers=[]
j=raw_input()
while i<7:
    print "At the top i is %d" % i
    numbers.append(i)
    i+=1
    print "Number now: ",numbers
    print "At the bottom i is %d" % i
print "The numbers: "
for num in numbers:
    print num
