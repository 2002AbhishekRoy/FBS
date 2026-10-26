print("This Program calculates the Simple Interest.")

p = int(input("Enter the Principal : "))
r = int(input("Enter the rate (in %) : "))
t = int(input("Enter the Time (in Years) : "))

si = (p * r * t) / 100

print("Simple Interest : ", si)
