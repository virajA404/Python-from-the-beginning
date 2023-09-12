#slicing - a method that extracts data from lists or tuples or strings

x = ['a', 'b', 'c','d', 'e', 'f']

#extracting from index 0 to index 3 in x and assigning to new list-y(or tuples or strings) 
y =x[0:3]
print(y)

#from the index 0 (beginning) to index 4
z=x[:4]
print (z)

#from mentioned index till the end of the list(or tuples or strings)
m = x[2:]
print (m)

#extracting the last index
n = x[-1]
print (n)

#extracting everything except the last index
p = x[:-1]
print (p)

#len() give the length of a data set
print(len(x))