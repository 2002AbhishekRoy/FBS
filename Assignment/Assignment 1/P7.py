import math
print("This Program find the Roots of a Quadratic Equation")

b = int(input("Enter the value of b : "))
a = int(input("Enter the value of a : "))
c = int(input("Enter the value of c : "))

d = (b**2) - (4*a*c)

if d < 0 :
    print("Imaginary Roots")

else:
    r1 = ((-b) + math.sqrt(d)) / 2 * a
    r2 = ((-b) - math.sqrt(d)) / 2 * a
    print("Root 1 : ", r1)
    print("Root 2 : ", r2)
