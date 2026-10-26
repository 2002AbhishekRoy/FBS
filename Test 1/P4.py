print("This program calculates the interior and exterior painting cost of the building.")

wall_area = float(input("Enter the area of one wall : "))
in_cost = float(input("Enter the cost of painting interior wall (per sq. unit) : "))
ex_cost = float(input("Enter the cost of painting exterior wall (per sq. unit) : "))

total_interior_area = 8 * wall_area
total_exterior_area = 7 * wall_area

interior_painting_cost = total_interior_area * in_cost
exterior_painting_cost = total_exterior_area * ex_cost

total_cost = interior_painting_cost + exterior_painting_cost


print("Total Interior Area : ", total_interior_area)
print("Total Exterior Area : ", total_exterior_area)
print("Interior Painting Cost        : Rs. ", interior_painting_cost)
print("Exterior Painting Cost        : Rs. ", exterior_painting_cost)
print("Total Painting Cost           : Rs. ", total_cost)
