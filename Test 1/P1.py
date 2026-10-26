import math
print("This Program calculates the area and perimeter of following figure.")

l = float(input("Enter the length : "))
b = float(input("Enter the breadth : "))
r = float(input("Enter the radius : "))

area = (2 * l * r) + ((1/2) * math.pi * (r**2))

perimeter = (2 * l) + (2 * r) + (math.pi * r)

print("Area : ", area)

print("Perimeter : ", perimeter)
