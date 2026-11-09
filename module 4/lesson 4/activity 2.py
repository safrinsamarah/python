import array as arr

scores = arr.array('i', [78,85,90,88,60])

print("scores: ", scores)
print("Number of scores: ",len(scores))
print("Last Score: ", scores[0])
print("Last score: ", scores[-1])

scores[2] = 89
print(scores)

scores.append(55)
scores.append(70)
print(scores)

scores.insert(0, 90)
print(scores)

scores.remove(55)
print(scores)

total = 0
for score in scores:
    total += score

print("Total scores: ", total)
average = total/len(scores)
print("Average: ", average)