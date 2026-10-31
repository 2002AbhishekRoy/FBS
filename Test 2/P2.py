def digit(n):
    c = 0

    while n > 0:
        n//=10
        c+=1

    return c



n = int(input("Enter the number : "))

if digit(n) == 3:
    d = n // 100
    d2 = n % 100
    d3 = d2 // 10
    m = d3 * 2
    third = d2 % 10
    h = third / 2

    if (d == m) and (d == h):
        print("Correct")

    else:
        print("Not Correct")
    
    
