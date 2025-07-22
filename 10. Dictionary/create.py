my_dict = {
    "Name":"SDC", "Age":20, "Marks":50.55,
}
print(my_dict)

dict_2 = {
    "Marks":[90,75,84.5]
}
print(dict_2)

# Key naming should be unique otherwise it will overwrite the previous key value
dict_3 = {
    "Age":25, "Age":30
}
print(dict_3) #it will print 30 as both the key names are same