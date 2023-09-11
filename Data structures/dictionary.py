#syntax
x = {'1000':"Colombo", '1300':"Kaluthara"}
x['1200'] = "Moratuwa"

#value can be a list 
x['fruits'] = ["Apple", "Mango", "Orange"] 

#value can be another dictionary 
x['books'] = {1998: "Harry Potter", 2000: "Lord of the ring" } 


# print(x)
# #to print the keys
# print(x.keys()) 

# #to print the values
# print(x.values()) 

# #accessing the dictionary
# y = x['1000'] 
# print(y) 

# #finding if the value is exists in the dictionary if not return 0
# z = x.get(1000, 0) 
# print(z)

#checking if the key is in (or not in) the dictionary
print("books" in x)

#delete the value from the dictionary
del x["1000"]
print(x)

#delete the entire dictionary
x.clear()
print(x)


r = {
    "a": ["Hello", "Hi", "Good morning"],
    "b": ["Bye", "Good night"],
    "c": 16
}

#List is a mutable object(can be changed after it is created)
#This list is passed by reference. 
#Every changers do to list will affect the original list
p = r['a']
p.append('Ayoubowan')
print(p)

#Data types are immutable objects(cannot be changed after it is created)
#This is passed by vale
#Every changers do to 'c' will not affect the original 'c' in dictionary
n = r['c']
n = 18

print(n)
print(r)