score = 0

def add_points(points):
    global score
    score += points
    print("current points: ", points)
    print("current score: ",score)

def lose_points(points):
    global score
    score -= points
    print("points lose: ", points)
    print("score lose: ", score)

earned = int(input("How many points did you earn? -> "))
lost = int(input("How many points did you lost? -> "))

add_points(earned)
lose_points(lost)

print("last score", score)