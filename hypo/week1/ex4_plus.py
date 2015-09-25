#!/usr/bin/env python
# coding=utf-8
#汽车数
cars = 100
#每个汽车的位置
space_in_a_car = 4
#司机数
drivers = 30
#乘客数
passengers = 90
#多少汽车没有司机
cars_not_driven = cars - drivers
#汽车可乘坐数为司机数
cars_driven = drivers
#总乘客数
carpool_capacity = cars_driven * space_in_a_car
#平均每辆车的乘客数
average_passengers_per_car = passengers / cars_driven

print "There aer",cars,"cars available."
print "There are only",drivers,"drivers available."
print "There will be",cars_not_driven,"empty cars today."
print "We can transport",carpool_capacity,"people today."
print "We have",passengers,"to carpool today."
print "We need to put about",average_passengers_per_car,"in each car."

