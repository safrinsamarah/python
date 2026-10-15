grid = [[0, 0, 0], [0, 0, 0]]
total = 0

for r in range(2):
    for c in range(3):
        num = int(input(f"Enter number for cell [{r+1}][{c+1}]: "))
        grid[r][c] = num
        total += num

print("Total sum:", total)