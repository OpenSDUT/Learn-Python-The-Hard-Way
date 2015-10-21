
def cheese_and_crackers(cheese_cout,boxes_of_crackers):
    print"You have %d cheeses!"% cheese_cout
    print"You have %d boxes of crachers!"%boxes_of_crackers
    print"Man that's enough for a party!"
    print"Get a blanket.\n"

print"We can just give the function numbers directly:"
cheese_and_crackers(20, 30)


print "OR, we can use variable from pur script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print"We can even do math inside too:"
cheese_and_crackers(10+20, 5+6)


print"And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers+100)

