#syntax 
x = {"hello","world",'hello','1','1'}

#adding key to a set
x.add("World")

#Set uses Hash function to find if a key is duplicate or not
#removing key from a set
x.remove("hello")
print(x)

#combining 2 sets
y = {"x","y","z", '1'}

#combining using UNION
z = x.union(y)
print(z)

#combining using PIPE operator
z1 = x | y
print(z1)

#subtracting 2 sets
p = x-y
print(p)

#how to check if a key is in the set
print("world"in x)
print("hello" not in y)