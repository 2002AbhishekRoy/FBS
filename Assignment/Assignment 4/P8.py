print("This Program print all integers upto n that aren’t divisible by 2 and 3.")

n = int(input("Enter the Limit : "))

for i in range(n):
    if i % 7 == 0 and i % 5 == 0:
        print(i)

        
