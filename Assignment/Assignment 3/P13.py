print("This Program input electricity unit charges and calculate total electricity bill according to the given condition.")

unit = int(input("Enter the unit charges : "))

if unit <= 50:
    price = 0.50 * unit
    total = price + (price * 20/100)

elif unit > 50 and unit <= 150:
    price = (0.5 * 50) + ((unit - 50) * 0.75)
    total = price + (price * 20/100)

elif unit > 150 and unit <=250:
    price = (0.50 * 50) + (100 * 0.75) + ((unit - 150) * 1.20)
    total = price + (price * 20/100)

elif unit > 250:
    price = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + ((unit - 250) * 1.50)
    total = price + (price * 20/100)

print("Units : ", unit)
print("Bill : ", price)
print("Total Bill : ", total)


