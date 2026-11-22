board = [
    ["House", "Tree","Rock", "Water"],
    ["Tree","Water","House","Rock"],
    ["Tree", "House", "Water", "Rock"],
    ["Rock","House","Tree","Water"]
]

print("First Row: ", board[0])
print("First row, second item: ", board[0][1])
print("Last item: ", board[-1][-1])

board[1][1] = "Castle"
print("Second row: ", board[1])

print("\n=====Board Game=====")
for row in board:
    for item in row:
        print(item, end="|")
    print( )

tree_count = 0

for board in row:
    for item in row:
        if item == "Tree":
            tree_count += 1
print("\nTotal number of trees: ", tree_count)