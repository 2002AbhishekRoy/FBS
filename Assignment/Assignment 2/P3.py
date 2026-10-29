print("This program converts distance from Feet and Inches into Meters and Centimeters.")

feet = float(input("Enter the distance in feet : "))
inches = float(input("Enter the distance in inches : "))

total_inches = (feet * 12) + inches

total_cm = total_inches * 2.54

meters = int(total_cm // 100)
centimeters = total_cm % 100

print("\nDistance is :",meters," Meter(s) and ",round(centimeters, 2)," Centimeter(s)")
