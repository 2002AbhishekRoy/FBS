p1 = float(input("Enter the price of Product 1 : "))
p2 = float(input("Enter the price of Product 2 : "))
p3 = float(input("Enter the price of Product 3 : "))
p4 = float(input("Enter the price of Product 4 : "))
p5 = float(input("Enter the price of Product 5 : "))

s = p1 + p2 + p3 + p4 +p5
gst = s * (18/100)
total = s + gst

print("Total Cost : ", s)
print("Total Cost after GST : ", total)
