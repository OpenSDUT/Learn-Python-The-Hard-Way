#!/usr/bin/env python
# coding=utf-8


class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sused",
                   "So I'll stop right there"])

buils_on_parade = Song(["They rally around the familly",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

buils_on_parade.sing_me_a_song()
