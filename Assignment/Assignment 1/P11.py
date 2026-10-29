import math
print("This Program find the area and circumference of circle.")

r = float(input("Enter the radius : "))

area = math.pi * (r**2)
cir = 2 * math.pi * r

print("Area : ", area)
print("Circumference : ", cir)
