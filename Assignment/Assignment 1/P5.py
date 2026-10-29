print("This Program calculates Compound Interest")

p = int(input("Enter the Principal : "))
r = int(input("Enter the Rate in (%) : "))
t = int(input("Enter the Time (in Years) : "))

ci = p * (1 + (r/100))**t

print("Compound Intrest : ", ci)
