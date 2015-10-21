#study drill 1:
print """
    range(stop) -> list of integers
    range(start, stop[, step]) -> list of integers
    
    Return a list containing an arithmetic progression of integers.
    range(i, j) returns [i, i+1, i+2, ..., j-1]; start (!) defaults to 0.
    When step is given, it specifies the increment (or decrement).
    For example, range(4) returns [0, 1, 2, 3].  The end point is omitted!
    These are exactly the valid indices for a list of 4 elements.
"""
#study drill 2:
element = []
element = range(1,6)
for i in element:
	print "element is %d"% i
#study drill 3:
print """
	list()	new empty list
	append(...)
       L.append(object) -- append object to end
   
   count(...)
       L.count(value) -> integer -- return number of occurrences of value
   
   extend(...)
       L.extend(iterable) -- extend list by appending elements from the iterable
   
   index(...)
       L.index(value, [start, [stop]]) -> integer -- return first index of value.
       Raises ValueError if the value is not present.
   
   insert(...)
       L.insert(index, object) -- insert object before index
   
   pop(...)
       L.pop([index]) -> item -- remove and return item at index (default last).
       Raises IndexError if list is empty or index is out of range.
   
   remove(...)
       L.remove(value) -- remove first occurrence of value.
       Raises ValueError if the value is not present.
   
   reverse(...)
       L.reverse() -- reverse *IN PLACE*
   sort(...)
       L.sort(cmp=None, key=None, reverse=False) -- stable sort *IN PLACE*;
       cmp(x, y) -> -1, 0, 1

"""
