#study 1:

print "This is study 1:"
def f1():
    print"this is a function."
    return one

def test():
    x = 100
    y = 50
    return x,y
m,n = test()
print "m = %d   n =  %d"%(m,n)

#study 2:
print "This is study 2:"
def add(a,b):
    print "ADDING..."
    return a + b
def subtract(a,b):
    print "SUBTRACTING..."
    return a - b
def multipy(a,b):
    print "MULTIPYING..."
    return a * b
def divide(a,b):
    print "DIVIDING..."
    return a / b

multiply2 = divide(divide(100,2),2)
subtract2 = multipy(multipy(90,2),multiply2)
add2 = subtract(subtract(78,4),subtract2)
what = add(add(30,5),add2)
print "The answer is %d"%what


#study 4:
print "This is study 4:"

print "'24 + 34 / 100 - 1023'"
print 24 + 34 / 100 - 1023
