#study drill 3:

#the function
def test(variable_one = 0,variable_two = 'a',variable_three = "False"):
    print"The value of variable_one is:%d" % variable_one
    print"The value of variable_two is %s" % variable_two
    print"The value of variable_three is",variable_three,"\n"

def return1():
    return 50;

#first
print"The first call"
test()

#second
print"The second call"
test(40,"second_value")

#third
print"The third call"
test(90,'jti',"True")

#fourth
print"The fourth call"
variable_one = 100
variable_two = 'false'
variable_three = 'True'
test(variable_one,variable_two,variable_three)

#fifth
print"The fifth call"
add = 40
test(add + variable_one)

#sixth
print"The sixth call"
test(variable_one-9,"value2",True)

#seventh
print"The seventh call"
x = return1()
test(x)

#eighth
print"The eighth call"
text(return1,"yzl",False)

