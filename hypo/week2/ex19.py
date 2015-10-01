#!/usr/bin/env python
# coding=utf-8
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You havee %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for party!"
    print "Get a bianket.\n"

print "We can just give the function numbers directiy."
cheese_and_crackers(20,30)

print "OR,we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

