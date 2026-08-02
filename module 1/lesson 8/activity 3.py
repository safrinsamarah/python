score = 0
q1 = input("What is the capital of France? : ").lower()
if q1 == "paris":
    score += 1
    print("Correct answer!")
else:
    print("Wrong answer! Try again.")
q2 = input("What is 5+7? : ").lower()
if q2 == "12":
    score += 1
    print("Correct answer!")
else:
    print("Wrong answer! Try again.")
q3 = input("Which language are we learning? : ").lower()
if q3 == "python ":
    score += 1
    print("Correct answer!")
else:
    print("Wrong answer! Try again.")

print(f"You got {score}/3")