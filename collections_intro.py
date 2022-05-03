
# lists are not immutable - meaning that they can change/ updated / edited
#shopping_list = ["eggs", "bread", "milk"]
#print(shopping_list)
#shopping_list.append("chocolate")
#print(shopping_list)

# Tuples are immutable - meaning that they cannot be changed
#essentials_tuple = ("bread, eggs")
#print(essentials_tuple)

# sets
#car_parts = {"wheels", "doors", "windows"}
#print(car_parts)

#car_parts.add("seats")
#print(car_parts)

# embedded lists (a list within a list)
#emb_list = [[1,2,3],[3,4,5]]
#for item in emb_list:
#    print(item)
#    for num in item:
#        print(num)


# Dictionaries

#dict_data = {1:{"name": "Fahimul", "course": "data"}, 2: {"name": "bob", "course": "dev"}}
#for item in dict_data.values():
#    print(item)

# to print 2

#    for key in item.values():
#        print (key)

user_prompt = True

while user_prompt:
    age = input("what is your age?")
    if age.isdigit():
        user_prompt = False
    else:
        print("please provide your age in digits")

print (f"your age is: {age}")