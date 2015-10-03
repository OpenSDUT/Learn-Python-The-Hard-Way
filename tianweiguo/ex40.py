#!/usr/bin/env python
# coding=utf-8
cities={'CA':'San Francisco','MI':'Destroit','FL':'Jacksonville'}
cities['NY']='New York'
cities['OR']='Portland'
def find_city(themap,state):
    if state in themap:
        return themap[state]
    else:
        return "Not Found!"
cities['_find']=find_city
while True:
    print "state?(ENTER to quit)",
    state=raw_input(">")
    if not state:break
    city_found=cities['_find'](cities,state)
    print city_found
