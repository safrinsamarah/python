fruit1 = {"mango", "banana", "apple"}
fruit2 = {"mango", "peach", "guava"}

# Set union - combine two or more sets
print("Set Union: ", fruit1.union(fruit2))

# Set intersection - finds the common sets
print("Set intersection: ", fruit1.intersection(fruit2))

# Set Difference - Keeps the set but removes the common items
print("Set Difference: ", fruit1.difference(fruit2))

# Symmetric Difference - keeps the value both of the sets but removes the common items
print("Smmetric difference: ", fruit1.symmetric_difference(fruit2))