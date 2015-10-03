def chese_and_crackers(chese_count,boxes_of_crackers):
	print "You have %d chese!"%chese_count
	print "You have %d crackers!"%boxes_of_crackers
	print "Is enougth?\n"

print "We can just give the funtion numbers directly:"
chese_and_crackers(20,30)

print "OR we can use the varibles from our script:"
amount_of_chese=10
amount_of_crackers=20
chese_and_crackers(amount_of_chese,amount_of_crackers)

print "We can even do math inside too"
chese_and_crackers(1+2,3+4)

print "And we can combin the two ,varables and math."
chese_and_crackers(amount_of_chese+5,amount_of_crackers+5)
