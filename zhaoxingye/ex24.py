print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
print poem

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five
print "This should be five: %d" % five
print "This should be five: %r" % five

def no_name(x):
    a=x*500
    b=a/1000
    c=b/100
    return a,b,c
x=10000
a,b,c=no_name(x)
print "a=%d,b=%d,c=%d."%(a,b,c)

x/=10
print "a=%d,b=%d,c=%d."%no_name(x)
