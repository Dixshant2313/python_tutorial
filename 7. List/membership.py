lst = [1,2,3,4,5]
check = int(input("Enter the number to check = "))
if check in lst:
    print("Number exists in the list")
else:
    print("Number does not exist in the list")



my_list = ["Onion","Potato","Tomato","Brinjal","Cabbage"]
veggie = input("Enter the vegetable to check : ").title()
if veggie not in my_list:
    print("Vegetable not found in bucket")
else:
    print("Vegetable found")
