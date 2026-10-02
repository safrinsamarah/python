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

def bonus_points(points):
    global score
    score += points
    print("points bonus: ", points)
    print("score bonus: ", score)

earned = int(input("How many points did you earn? -> "))
lost = int(input("How many points did you lost? -> "))
bonus = int(input("How any points did you got bonus? ->"))

add_points(earned)
lose_points(lost)
bonus_points(bonus)

print("last score", score)