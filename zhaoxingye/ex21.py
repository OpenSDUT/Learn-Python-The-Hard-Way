def add(a,b):
    print "Adding %d + %d = " %(a,b)
    return a+b
def jian(a,b):
    print "Jianning %d - %d = "%(a,b)
    return a-b
def cheng(a,b):
    print "Chenging %d * %d = "%(a,b)
    return a*b
def chu(a,b):
    print "Chuing %d / %d = "%(a,b)
    return a/b

print "Let's do some math with some function."

age=add(30,5)
height=jian(78,4)
weight=cheng(90,2)
iq=chu(100,2)

print "Age: %d. Height: %d. Weight: %d. iq: %d."%(age,height,weight,iq)

print "what=add(age,jian(height,cheng(weight,chu(iq,2))))"

what=add(age,jian(height,cheng(weight,chu(iq,2))))

print "what = %d." % what
