#Names,Variables,Code,Functions

#This one is like your script with argv
def print_two(*args):
    arg1,arg2 = args
    print"arg1:%r,arg2:%r" %(arg1,arg2)

#ok,thst *args is actually pointless,we can just do this
def print_two_again(arg1,arg2):
    print"arg1:%r,arg2:%r" %(arg1,arg2)

#this jua=st takes one argument
def print_one(arg1):
    print"arg1:%r" % arg1

#this one takes no arguments
def print_none():
    print"I got nothing."

print_two("Zed","Shaw")
print_two_again("person1","person2")
print_one("only_one")
print_one("only one just")
print_none()
