def calculating_scores (points,bonus):
    final_score = points + bonus
    return final_score

points = int(input("Enter your points earned so far: "))
bonus = int(input("Enter your bonus points: "))

score = calculating_scores(points,bonus)

print("Final score:",score)
