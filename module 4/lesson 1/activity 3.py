tasks = ["Homework", "Reading", "Exercise", "Python", "Cleaning"]

print("Total tasks:", len(tasks))
print(tasks[0])
print(tasks[-1])

# Add
tasks.append("Writing")
tasks.insert(2, "Drawing")

# Update a task
tasks[0] = "Math Homework"

# Remove task
tasks.remove("Exercise")
tasks.pop(1)

# Sort and display task
tasks.sort()
print("\nSorted Tasks:")
for task in tasks:
    print(task)

# Display a portion using slicing
print("\nFirst three tasks:", tasks[0:3])
