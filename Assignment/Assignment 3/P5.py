print("This Program check whether the triangle is equilateral, isosceles or scalene triangle.")

a = int(input("Enter the first side : "))
b = int(input("Enter the second side : "))
c = int(input("Enter the third side : "))

if a == b and b == c and c == a:
    print("Equilateral Triangle")

elif a == b or b == c or c == a:
    print("Isosceles Trinagle")

elif a != b and b != c and c != a:
    print("Scalene Triangle")
