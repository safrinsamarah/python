mylist = [233, 12.33, "python", True]
print(mylist)

#length of the list
print("length: ", len(mylist))

#Accessing the items into index
print(mylist[1])
print(mylist[0])
print(mylist[-1])

#slicing
print("slicing: ", mylist[1:3])

#adding an item
mylist.append("Programming")
print(mylist)

#removing an item
mylist.pop(2)
print(mylist)

number_list = [32,43,66,55,99]
number_list.sort()
print(number_list)