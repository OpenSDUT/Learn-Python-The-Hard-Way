#!/usr/bin/env python
# coding=utf-8
print("let's practice everything")
print("you'd need to know about escapes with \\that do \n newlines and \t tabs.")

poem = '''\tThe lovely world with logic so firmly planted
cannot discern\n the needs of love
nor comprehend passion from intuition
and requires and explanation
\n\twhere there is none.
'''

print("------")
print(poem)
print("------")

five = 10-2+3-6
print("This should be five %s"%five)

def secret_formula(started):
    jelly_bean = started*500
    jars = jelly_bean /1000
    crates = jars /100
    return jelly_bean,jars,crates
start_point = 10000
beans,jars,crates = secret_formula(start_point)
print("with a starting point of%d"%start_point)
print("we'd have %d beans,%d jars,and %d crates"%(beans,jars,crates))

start_point = start_point/10
print("we can do that this way")
print("we have %d beans,%d jars,and %d crates"%secret_formula(start_point))
