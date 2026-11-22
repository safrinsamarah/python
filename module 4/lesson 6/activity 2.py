students = {
    "Amar": {
        "Math": 90,
       "English": 87,
       "Science": 88
    },

    "Rahim": {
        "Math": 88,
        "English": 88,
        "Science": 77
    },

    "Sara": {
        "Math": 99,
        "English": 77,
        "Science": 78
    }
}

print("Amar's math: ", students["Amar"]["Math"])
print("Sara's English: ", students["Sara"]["English"])

students["Amar"]["Math"]: 94
print("Amar's updated marks: ", students["Amar"]["Math"])

students["Sara"]["ICT"]: 88
print(students["Sara"])

print("\n=====Student's ReportCard======")
for name, subjects in students.items():
    print("\nStudent: ",name)
    total = 0
    for subject, score in subjects.items():
        print(f"{subject} -> {score}")
        total += score
        print("Total Marks: ", total)
    
    avg = total/len(subjects)
    print("Average: ", round(avg, 2))

