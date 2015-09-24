#!/usr/bin/env python
# coding=utf-8
formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one","two","three","four")
print formatter % (True,False,False,True)
print formatter % (formatter,formatter,formatter,formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
#至于引号的工作原理，只要能区分完整字符串就是
#比如如果字符串中包含单引号，那么就可以用双引号来标记完整字符串
#而如果字符串中包含双引号，那么就可以用单引号来标记
#如果都有，就可以用"""字''符""串""" 三个双引号或者单引号标记
#突然想到，如果包含三个连续引号的字符串肿么办_(:з」∠)_
#然后自己尝试发现，只需要在和标记引号相同的引号加个转义字符就好了
