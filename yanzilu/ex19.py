#Functions And Variables

def chese_and_crackers(cheese_count,boxes_of_crackers):
    print "You have %d cheeses!" %cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party"
    print "Get a blanket.\n"

print "We can just give the function numbers directly:"
chese_and_crackers(20,30)


print"OR,we can use variables from our script:"
amount_of_cheese = 10;
amount_of_crackers = 50;
chese_and_crackers(amount_of_cheese,amount_of_crackers)

print"We can even do math inside too:"
chese_and_crackers(10+20,5+6)

print"And can combin the two,variables and math:"
chese_and_crackers(amount_of_cheese+100,amount_of_crackers-20)
