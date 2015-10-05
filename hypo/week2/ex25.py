#!/usr/bin/env python
# coding=utf-8
def break_words(stuff):
    """this function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """sorts the words."""
    return sorted(words)

def print_first_word(words):
    """print the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word(words):
    """print the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """takes in full sentence and returns the sorten words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """print the firstrst and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


