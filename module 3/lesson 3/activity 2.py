def max_of_three(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>= a and b>= c:
        return b
    else:
        return c

max_num = max_of_three(10,35,23)
print(max_num)
