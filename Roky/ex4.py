#coding:utf-8

#车的数量;
cars = 100

#一辆车内的空间;
space_in_a_car = 4.0

#司机数量;
drivers = 30

#旅客数量;
passengers = 90

#没有人驾驶的汽车数量;
cars_not_driven = cars - drivers

#有人驾驶的汽车数量;
cars_driven = drivers

#拼车容量;
carpool_capacity = cars_driven * space_in_a_car

#每辆(有人驾驶的)车的平均旅客数;
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
