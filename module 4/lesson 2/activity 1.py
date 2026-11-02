my_tuple = (25.6, 25, "python", True , 25)
print("Tuple:", my_tuple)

#length
print("Length: ", len(my_tuple))

#accessing a number through indexing
print(my_tuple[2])
print("First item:", my_tuple[0])
print("Last item:", my_tuple[-1])

#Iterating through loop
for item in my_tuple:
    print(item)

#Unpacking
item1, item2, item3, item4, item5 = my_tuple
print("item1: ", item1)
print("item2: ", item2)
print("item3: ", item3)
print("item4: ", item4)
print("item5: ", item5)

#Count matching values
print("Count of 25: ", my_tuple.count(25))