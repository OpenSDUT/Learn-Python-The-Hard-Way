name = 'Roky Zevon'
age = 21 # not a lie
height = 178 # centimeter
weight = 63 # kilogram
eyes = 'Amber'
teeth = 'White'
hair = 'Black'

print "Let's talk about %s." % name
print "He's %r centimeter tall." % height
print "He's %r kilogram heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)
