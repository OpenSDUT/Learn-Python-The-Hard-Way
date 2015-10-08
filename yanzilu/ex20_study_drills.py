# study drills 4

from sys import argv
script,input_file = argv
current_file = open(input_file)

#close(),close the file

#fileno(),
#flush(),
#isatty(),


#next(),x.next(),the next value,or raise StopIteration
print current_file.next()


#read([size]),read at most size bytes,returned as a string.
#readline(),return the next line from the file,as a string.
#readlines([size]),



#seek(),
#tell(),current file position,an integer(may be a long integer).
print current_file.tell()

current_file.close()
#truncate([size]),

#write(str),Write string str to file.

#writelines(sequence_of_strings),Write the strings to the file.
print"please input the file name"
file1 = raw_input()
file2 = open(file1,'w')
file2.write("hdsgyuewjkdhf\nuhdcyuwhu")
#seek()
file2.seek(0)
#close()
file2.close()


