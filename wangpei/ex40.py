#!/usr/bin/env python
# coding=utf-8
mystuff = {'apple':'I am apples'}
print(mystuff['apple'])

def apple():
    print("I am apples")
    tangerine = "Living reflection of a dream"

class Mystuff(object):
    def __init__(self):
        self.tangerine = "And now a thousand years between"
        def apple(self):
            print("I am classy apples")

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you","I don't want to get sued","So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family","With pockets full of shells"])
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
