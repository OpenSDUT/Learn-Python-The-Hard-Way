formatter_1 = '%s %s %s %s'
formatter_2 = '%r %r %r %r'

print formatter_1 % (1,2,3,4)
print formatter_2 % (1,2,3,4)
print formatter_1 % ("one","two","three","four")
print formatter_2 % ("one","two","three","four")
print formatter_1 % (formatter_1,formatter_1,formatter_1,formatter_1)
print formatter_2 % (formatter_2,formatter_2,formatter_2,formatter_2)
print formatter_1 % ("I love you","I love you","I love you","I love you")
print formatter_2 % ("I love you","I love you","I love you","I love you")
