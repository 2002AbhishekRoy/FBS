print("This program calculates the third angle of a triangle.")

angle1 = float(input("Enter the first angle : "))
angle2 = float(input("Enter the second angle : "))

if angle1 <= 0 or angle2 <= 0:
    print("Angles must be greater than 0°.")

elif (angle1 + angle2) >= 180:
    print("The sum of the first two angles cannot be 180° or more!")
    
else:
    angle3 = 180 - (angle1 + angle2)
    print("The third angle of the triangle is : ", angle3)
