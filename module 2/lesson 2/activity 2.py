secret = 42
guess = None

while guess != secret:
    guess = int(input("Enter your guess (1 - 100): "))
    if guess < secret:
        print("Too low.👇")
    elif guess > secret:
        print("Too high.☝️")

print("Correct Answer! you got the number.")