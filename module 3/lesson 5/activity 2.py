import random
import math

number = random.randint(1,15)
square = number ** 2

print("Find the square root of: ",square)

guess = int(input("Your guess: "))
correct_answer = math.sqrt(square)

if guess == correct_answer:
    print("Correct!")
else:
    print("Wrong. the answer is", correct_answer)