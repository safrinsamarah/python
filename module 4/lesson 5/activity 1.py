# step 1 create and access the grade dictionary
grade = {
    "Math": 98,
    "Science": 92,
    "English": 79,
    "Geography": 86
}

print("Grades:", grade)
print("Math: ", grade["Math"])
print("English: ", grade.get("English"))

#Step 2 add, update and remove subjects
grade["Religion"] = 77
print(grade)

grade["English"] = 88
print(grade)

grade.pop("Religion")
print(grade)

#step 3 display and analyze grades
for subject,score in grade.items():
    print(f"{subject} -> {score}")

total = 0

for score in grade.values():
    total += score

print("total score: ", total)

average = total / len(grade)
print("average: ", average)

#step 4 find high number
print("=====High Score=====")
for subject, score in grade.items():
    if score >= 90:
        print(f"{subject} -> {score}")