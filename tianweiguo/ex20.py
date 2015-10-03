from sys import argv
script,input_file=argv

def print_all(f):
	print f.read()
def print_a_line(line_count,f):
	print line_count,f.readline()
def rewind(f):
	f.seek(0)

current_file=open(input_file)

print "First we print all the file!"

print_all(current_file)

print "Now let's rewind"

rewind(current_file)

print "let's print three lines:"

line_count=1
print_a_line(line_count,current_file)

line_count+=1
print_a_line(line_count,current_file)

line_count+=1
print_a_line(line_count,current_file)


