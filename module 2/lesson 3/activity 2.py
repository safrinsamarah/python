first = [3,5,7]
second = [2,4,6]

i = 0
while i < len(first):
    j = 0
    while j < len(second):
        result = first[i] * second[j]
        print(f"{first[i]} * {second[j]} = {result}")
        j = j + 1
    i = i + 1
