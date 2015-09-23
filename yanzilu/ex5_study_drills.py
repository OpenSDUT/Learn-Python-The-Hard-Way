#study drill 1
name = 'Aed A.Shaw'
age = 18
height = 80
weight = 150
eyes = 'Blue'
teeth = 'White'
hair = 'Black'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." %(eyes,hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %d,%d,and %d I get %d." %(
        age,height,weight,age+height+weight)

# study drill 2
print "-------------------------------------------"
print "Let us try %r" % "who is that?"
print "Let us try again %r" % 'who is that?'
print "Let us try %"
print "Let us try %c" % "j"
print "Let us try %02d and %05d" %(345,6)
print "Let us try %u" % -367
print "Let us try %o" % 9
print "Let us try %c" %108

# study drill 4
print "1 inches equal 2.54 centimeter \n 1 pounds equal 0.4536 kilogram "

my_height_cm = height * 2.54
my_weight_kg = weight * 0.4536

print "He's %d centimeters tall." % my_height_cm
print "He's %d kilogram heavy." % my_weight_kg
