size = 8
 
for row in range(size):
    for col in range(size):
        if (row+col)%2 == 0:
            print("x",end=" ")
        else:
            print("o",end=" ")
    print()