num_of_rows = int(input("Enter the number of rows: "))

for row in range(num_of_rows):
    for col in range(num_of_rows):
        if row == 0 or row == num_of_rows -1 or col == 0 or col == num_of_rows -1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    
    print( )