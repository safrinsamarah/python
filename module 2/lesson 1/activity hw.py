gpa = float(input("Enter your GPA (0.0 - 4.0): "))
math_score = int(input("Enter your Math score (0 - 100): "))
leadership = input("Do you have leadership experience? (Y/N): ").upper()

if gpa >= 3.0:
    print("✅ GPA requirement met.")

    if math_score >= 85:
        print("✅ STEM path eligible.")

        if leadership == "Y":
            print(" +5 scholarship points.")
        else:
            print("No leadership bonus.")
            
    else:
        print(" Math score too low.")

else:
    print("GPA below threshold.")