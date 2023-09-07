x = [13,53,56,22]
z = [34,56,22,67]

#print values
y= x[0]
print(y)

#change values
x[2] = 49
print(x)

#add values to the end of the list
x.append(100)
print(x)

#add values to anywhere in the list
x.insert(1,200)
print(x)

#remove values from the list
x.remove(53) #give the value
print(x)    
# or
x.pop(3)    #give the index
print(x)

#adding 2 lists
add = x + z
print(add)

#checking if some value is in the list(gives a boolean value)
print(200 in x)

#checking if some value is not in the list(gives a boolean value)
print(203 not in x)     #in - always returns a boolean value