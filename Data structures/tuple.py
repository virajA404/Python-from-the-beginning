#Syntax
viraj = ("viraj", 25, "Colombo", "Sri Lanka")

print(type(viraj))
print(viraj)

#accessing values in tuple
name = viraj[0]
print(name)

#count of a value in a tuple
print(viraj.count(25))

#expanding tuples - assigning values of tuple to variables
name, age, city, country = viraj
print(name, age, city, country)