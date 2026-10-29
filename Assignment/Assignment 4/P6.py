print("The Program check if a given number is prime number or not.")

n = int(input("Enter a number : "))

c= 0

if n <=1:
    print("Not Prime")

else:
    for i in range(2,n):
        if n % i == 0:
            c = 1
            break


    if c == 1:
        print("Not Prime")
    else:
        print("Prime")
