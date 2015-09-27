# study drill 2
from sys import argv

script,user_name = argv
prompt = "please input: "

print "Hi %s,I'm the %s script."%(user_name,script)
print "I'd line to ask you a few questions."
print "Do you like me %s?" % user_name
like = raw_input(prompt)

print "Where do you live %s?" %user_name
live = raw_input(prompt)
tishi = ">>"
print "What kind od computer do you have?"
computer = raw_input(tishi)

print """
Alright,so you said %r about liking me.
You live in %s.I had went there.
And you have a %s computer.That's great!!
""" %(like,live,computer)
