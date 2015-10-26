# -*- coding:utf-8 -*-
#Exercise 37:Symbol Review

print """
ONE Keywords:

KEYWORD           EXAMPLE
and					True and False == False
as					with X as Y:pass
assert				assert False,"Error!"
break				while True:break
class				class Person(object)
continue			while True:continue
def					def x():
elif				if: X;elif:Y;else:J
else				if:X;else:J
except				except ValueError,e:print e
exec				exec 'print "hello"'
finally				finally:pass
for					for X in Y:pass
from				import x from y
global				global X
if					if:X;else:J
import				import os
in					for X in Y:pass;also 1 in[1] == True
is					1 is 1 == True
lambda				s = lambda y:y ** y;s(3)
not					not True == False
or					True or False == True
pass				def empty():pass
print				print "this string"
raise				raise ValueError("No")
return				def X():return Y
try					try:pass
while				while X:pass
with				with X as Y:pass
yield				def X():yield Y;X().next()



Data Types

TYPE			EXAMPLE

True				True od False == True
False				False and True == False
None				x = None
string				x = "hello"
numbers				i = 100
floats				y = 5.8
lists				list = [1,2,3,4]
dicts				e = {'x':1,'y':2}


String Escape Sequences

ESCAPE			DESCRIPTION

\\					Backslash
\'					Single-quote
\"					Double-quote
\a					Bell
\b					Backspace
\f					Formfeed
\n					Newline
\r					Carriage
\t					Tab
\v					Vertical tab


String Formats

ESCAPE			EXAMPLE
%d					"%d" % 45 == '45'
%i					"%i" % 45 == '45'
%o					"%o" % 1000 == '1750'
%u					"%u" % -1000 == '-1000'
%x					"%x" % 1000 == '3e8'
%X					"%X" % 1000 == '3E8'
%e					"%e" % 1000 == '1.000000e + 0.3'
%E					"%E" % 1000 == '1.000000E + 0.3'
%f					"%f" % 10.34 == '10.340000'
%F					"%F" % 10.34 == '10.340000'
%g					"%g" % 10.34 == '10.34'
%G					"%G" % 10.34 == '10.34'
%c					"%c" % 34 == '"'
%r					"%r" % int == "<type 'int'>"
%s					"%s there" % 'hi' == 'hi there'
%%					"%g%%" % 10.34 == '10.34%'


Operators

OPERATOR				EXAMPLE
+						2 + 4 = 6
-						2 - 4 = -2
*						2 * 4 = 8
**						2 ** 4 = 16
/						2 / 4.0 = 0.5
//						2 // 4.0 = 0.0
%						2 % 4 = 2
<						2 < 4 == True
>						2 > 4 == False
<=						2 <= 4 == True
>=						4 >= 4 == True
==						4 == 5 == False
!=						4 != 5 == True
<>						4<>5 == True
()						len('hi') == 2
[]						list = [1,2,3]
{}						dict = {'x':5,'name':"xiaoming"}
@						@classmethod
,						range(0,10)
:						def f():
.						self.x = 10
=						y = 10
;						print "hi";print "there"
+=						x = 1;x += 2;x = 3
-=						x = 5;x -= 2;x = 3
*=						x = 3;x *= 3;x = 9
/=						x = 6;x /= 2;x = 3
//=						x = 7;x /= 2;x = 3
%=						x = 7;x %= 2;x = 1
**=						x = 2;x **= 3;x = 8


"""
