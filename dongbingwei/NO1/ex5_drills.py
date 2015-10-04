# first delete the 'my_'

name = 'Zed A. Shaw'
age = 35  # not a lie
height = 74  # inches
weight = 180  # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right

print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight
)

# 在python中格式化字符%r，表示打印的是对象，什么都打印
# there will print 'text 'Brown''
print 'text %r' % hair


# %s    字符串 (采用str()的显示)
# %r    字符串 (采用repr()的显示)
# %c    单个字符
# %b    二进制整数
# %d    十进制整数
# %i    十进制整数
# %e    指数 (基底写为e)
# %E    指数 (基底写为E)
# %f    浮点数
# %F    浮点数，与上相同
# %g    指数(e)指数或浮点数 (根据显示长度)
# %G    指数(E)或浮点数 (根据显示长度)
