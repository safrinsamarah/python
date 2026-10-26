subjects = [
    "Math",
    "English",
    "Physics",
    "Computer Science"
]
print("Total subjects: ",len(subjects))
print("First subject: ",subjects[0])
print("Second subjects: ",subjects[-1])

print("Priority subjects: ",subjects[ :2])
print("other subjects: ", subjects[-2: ])

subjects[1] = "ICT"
print(subjects)

subjects.append("chemistry")
print(subjects)
subjects.insert(1,"Biology")
print(subjects)

subjects.remove("Physics")
print(subjects)
subjects.pop(2)
print(subjects)

new_subject = input("Enter a new subject: ")
subjects.append(new_subject)
print(subjects)