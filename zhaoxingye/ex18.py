def print_two(*args):
    arg1,arg2=args
    print "arg1: %r.arg2: %r." % (arg1,arg2)

def print_three(arg1,arg2,arg3):
    print "arg1: %r.arg2: %r.arg3: %r." % (arg1,arg2,arg3)
def print_one(arg1):
    print "arg1: %r." % arg1
def print_none():
    print "There're nothing."

print_two("zhao","xingye")

print_three("I","love","you!")

print_one("zhaoxingye")

print_none()
