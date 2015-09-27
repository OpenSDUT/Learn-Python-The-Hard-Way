#!/usr/bin/env python
# coding=utf-8
people = 20
cats = 30
dogs = 15

if people<cats:
    print("too many cats!the world is doomed")
if people>cats:
    print("not many cats,the world is saved")
if people<dogs:
    print("the world is drooled on!")
if people>dogs:
    print("the world is dry")
dogs+=5

if people>=dogs:
    print("people are less than or equal to dogs")
if people == dogs:
    print("people are dogs")
