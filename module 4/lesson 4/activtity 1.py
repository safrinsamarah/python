import array as arr

numbers = arr.array('i',[1,2,3,4,5,6])
print(numbers)

print(numbers[1])
print(numbers[2:5])

for num in numbers:
    print("Value: ", num)

#Insertion -> insert a value in a particular index
numbers.insert(2,10)
print(numbers)

#Remove
numbers.remove(5)
print(numbers)