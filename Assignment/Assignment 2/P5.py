print("This Program calculates selling price of book based on cost price and discount.")

cp = int(input("Enter the cost price of the Book : "))
discount = int(input("Enter the discount (%) : "))
print("We assume that the book is sold at Rs. 20 profit")

price = cp + 20
d = price * (discount/100)
sp = price - d

print("Selling Price : ", sp)
