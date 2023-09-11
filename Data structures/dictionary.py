#syntax
x = {'1000':"Colombo", '1300':"Kaluthara"}
x['1200'] = "Moratuwa"

#value can be a list 
x['fruits'] = ["Apple", "Mango", "Orange"] 

#value can be another dictionary 
x['books'] = {1998: "Harry Potter", 2000: "Lord of the ring" } 


print(x)
#to print the keys
print(x.keys()) 

#to print the values
print(x.values()) 

#accessing the dictionary
y = x['1000'] 
print(y) 

#finding if the value is exists in the dictionary if not return 0
z = x.get(1000, 0) 
print(z)

#delete the value from the dictionary
del x["1000"]
print(x)

#delete the entire dictionary
x.clear()
print(x)