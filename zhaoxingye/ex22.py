print    # shuchu , use '',"" or """ """
#        # xiushi houmian de daima
+ - * / < > >= %  # method of use
x = 10 y = 'zhaoxingye' # bianliang de fuzhi
%s %d %r # daibiao de hanyi
x='zhao' y='xingye' z=x+y='zhaoxingye' 
a='a' b='b' c='c' d=a+b*2+c='abbc' # + keyi lianjie zifuchuan
%s %r de qubie # %s shibie shuchu , %r yuanyang shuchu
/  # zai shuchu guocheng zhong / de zuoyong
age=raw_input()   # zai jianpan jieshou yige zhi gei bianliang 'age'
age=raw_input("How old are you?") # zai jiushou zhi de tongshi , shuchu "How old are you?", tishi zuoyong
from sys import argv
script,first,second,third=argv 
# jieshou san'ge zhi fenbie gei 'first','second','third' 
print """
zhaoxingye
I love you
Do you konw?
"""
#  """keyi dingyi duohang zifuchuan
txt=open(filename)   # jiang "filename" dakai
print txt.read()     # shuchu wenjian zhong de dongxi
txt.close()          # guanbi and baocun wenjian
txt=open(filename,'w') # dakai wenjian,zhunbei xieru wenjian 'w'=write
txt.truncate()       # qingkong wenjian
txt.seek(0)          # jiang zhizhen zhixiang wenjiantou
txt.readline()       # read wenben de mouyihang,shunxu read
line1=raw_input("line1:")
line2=raw_input("line2:")
line3=raw_input("line3:")
txt.write(line1)
txt.write("\n")
txt.write(line2)
txt.write("\n")
txt.write(line3)
txt.write("\n")
# fenbie shuru sanhang shuju,xieru wenjian zhong
from os.path import exists
print "%r" % exists(filename.txt) # panduan wenben 'filename.txt' shifou cunzai ,cunzai -> 'TURE' ,not cunzai -> 'FALSE'
a_1=open(file_1)
b_1=a_1.read()
a_2=open(file_2,'w')
a_2.write(b_1)         #  file_1  copy  dao  file_2
def hanshuming(a,b):
    .....
    .....
    print "...."
    return a+b
c=hanshuming(a,b)
d=hanshuming(1,2)
e=hanshuming(a+1,b+2)
f=hanshuming(1+2,3+4)
# def dingyi hanshu,keyi use 'return' fanhui zhi
def add(a,b):
    return a+b
def jian(a,b):
    return a-b
def cheng(a,b):
    return a*b
def chu(a,b):
    return a/b
a=1
b=2
c=3
d=4
e=5
what=add(a,jian(b,cheng(c,chu(d,e))))  # hanshu de taoyong
    









