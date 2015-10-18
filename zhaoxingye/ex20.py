from sys import argv

script , file_test = argv

def print_all(name):
    print name.read()

#def rewind(name):
 #   name.seek(0)

def print_line(line,name):
    print line,">>",name.readline()

def file_close(name):
    name.close()

file_open=open(file_test)
print_all(file_open)

# rewind(file_open)

file_close(file_open)

file_open_again=open(file_test)

line=1
print_line(line,file_open_again)

line+=1
print_line(line,file_open_again)

line+=1
print_line(line,file_open_again)

file_close(file_open)
