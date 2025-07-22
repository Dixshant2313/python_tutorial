a = 10 #integer datatype
print(type(a))

b = 5.2 #float 
print(type(b))

name = "SDC" #string datatype
print(type(name))

imaginary = 6 + 5j #complex datatypes
print(type(imaginary))

print(a>b) #Boolean datatype

d = range(0,10)
print(type(d)) #Range datatype

fruits = ["apple", "banana", "mango"]
print(type(fruits)) #list

veggies = ("onion", "aloo", "tamatar")
print(type(veggies)) #tuple

stationary = {"pen", "pencil", "sharpner"}
print(type(stationary)) #set

subjects = frozenset({"english", "maths", "chemistry"})
print(type(subjects)) #frozen set


my = (1,5,3,4)
print(my)
print(type(my))

simple = {1,1,2,4,5,7,7,4}
print(simple)
print(type(simple))

data = {"name": "Shreya", "age": 12}
print(type(data))                       #dictionary datatype

person_name = "Yashika"
print(person_name[-2])