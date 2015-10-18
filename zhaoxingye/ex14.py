from sys import argv

script, user_name = argv
aaa = '>'
bbb = '>>'
ccc = '>>>'

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(aaa)

print "Where do you live %s?" % user_name
lives = raw_input(bbb)

print "What kind of computer do you have?"
computer = raw_input(ccc)

print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
""" % (likes, lives, computer)
