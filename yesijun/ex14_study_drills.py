# study drill 1
from sys import argv

script, user_name, age = argv
input_value = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?, and age is %s" % (user_name, age)
likes = raw_input(input_value)

print "Where do you live %s" % user_name
lives = raw_input(input_value)

print "What kind of computer do you have?"
computer = raw_input(input_value)

print """
Alright so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
