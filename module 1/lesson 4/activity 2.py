player1 = 987
player2 = 999
player3 = 12321

avg = (player1+player2+player3)/3
print(f"Average number is {round(avg,2)}")

#Compare the scores
print(f"Player1 < Player2: {player1 < player2}")
print(f"player2 > Average: {player2 > avg}")
print(f"Is player3 has the highest score? {player3 > player1 and player3 > player2}")

#Find the highest score
highest = max(player1,player2,player3)
print(f"Highest score is {highest}")