i=0
number = []

while i < 6:
	print "At the top i is %d" % i
	number.append(i)

	i=i+1
	print "Number now:", number
	print "At the bottom i is %d" % i


print "The number:"

for num in number:
	print num

