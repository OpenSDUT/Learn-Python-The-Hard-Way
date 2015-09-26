#coding:utf-8

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."


#'\t'是制表符;
#第14行表示了在""""""中文本编辑时获取的回车也是'\n'
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#单引号测试;
#结论：目前看来单引号和双引号一个效果;
fat_cat =''' 
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''
print fat_cat
