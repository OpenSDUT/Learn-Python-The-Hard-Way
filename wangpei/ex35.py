#!/usr/bin/env python
# coding=utf-8
from sys import exit

def gold_rooms():
    print("This room is full od gold.how much do you take")

    next = input(">")
    if "0" in next or "1" in next:
        how_much =int(next)
    else:
        dead("man,learn to type a number contains 0 or 1")
        start()
    if how_much<50:
        print("nice,you're not greedy,you win!")
        exit(0)
    else:
        dead("you greedy bastard")
def bear_rooms():
    print("there is a bear here")
    print("the bear has a brunch of honey")
    print("the fat bear is in front od another door")
    print("how are you going to move the bear")
    bear_moved = False

    while True:
        next = input(">")
        if next=="take money":
            dead("the bear looks at you then slaps your face off.")
        elif next=="taunt bear" and not bear_moved:
            print("the bear has moved from the door.you can go through it now.")
            bear_moved=True
        elif next=="taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off")
        elif next=="open the door" and bear_moved:
            gold_rooms()
        else:
            print("I got no idea what that means.")
def cthulhu_room():
    print("here you see the great evil cthulhu")
    print("he,it,whatever stares at you and you go insane")
    print("do you flee for your life or eat your head?")
    
    next = input(">")
    if "flee" in next:
        start()
    elif "head" in next:
        dead("well that was tasty!")
    else:
        cthulhu_room()
def dead(why):
    print(why,"good job!")
    exit(0)
def start():
    print("you are in a dark room.")
    print("there is a door to your right and left.")
    print("which one do you take?")
    next = input(">")

    if next=="left":
        bear_rooms()
    elif next=="right":
        cthulhu_room()
    else:
        dead("you stumble around the room util you starve")

if __name__=='__main__':
    start()
