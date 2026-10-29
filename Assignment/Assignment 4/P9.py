print("This Program print all numbers in a range divisible by a given number.")

a = int(input("Enter the number : "))
n = int(input("Enter the Limit : "))

for i in range(n):
    if i % a == 0:
        print(i)

        
