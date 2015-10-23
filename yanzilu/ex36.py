# -*- coding:utf-8 -*-
# A small game
from random import randint

def ran_num():
	random_number = randint(1,3)
	return random_number

def per_num():
	print "please input 'stone','scissors' or 'cloth'"
	person_num = raw_input()
	if person_num == "stone":
		person_number = 1
	elif person_num == 'scissors':
		person_number = 2
	elif person_num == 'cloth':
		person_number = 3
	else:
		print "please input right!!"
		exit(0)
	return person_number

def start():
	print "Let's play a small game,are you ready? True or False?"
	status = raw_input("> ")
	while True:
		if status == 'False':
			exit(0)
		else:
			random_number = ran_num()
			person_number = per_num()
			if random_number == 1 and person_number == 2:
				print "You lose!"
			elif random_number == 2 and person_number == 3:
				print "You lose!"
			elif random_number == 3 and person_number == 1:
				print "You lose!"
			elif random_number == person_number:
				print "draw!!"
			else:
				print "You win!"
			print "Are you continue?True or False?"
			status = raw_input("> ")

start()
