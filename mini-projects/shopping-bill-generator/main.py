""" Shopping Bill Generator"""

customer_name = input("Enter customer name: ")

print()
print("Available Products")
print()

print("1. Rice  - ₹60/Kg")
print("2. Sugar - ₹45/Kg")
print("3. Milk  - ₹30/L")
print("4. Bread - ₹40/pieces")
print("5. Eggs  - ₹8 each")

print()
print("Enter quantity:")
print()

rice_qty = int(input("Rice (kg): "))
sugar_qty = int(input("Sugar (kg): "))
milk_qty = int(input("Milk (L): "))
bread_qty = int(input("Bread: "))
eggs_qty = int(input("Eggs: "))
print()

rice_total = rice_qty * 60
sugar_total = sugar_qty * 45
milk_total = milk_qty * 30
bread_total = bread_qty * 40
eggs_total = eggs_qty * 8

total_bill = rice_total + sugar_total + milk_total + bread_total + eggs_total
 
discount = 0 

if total_bill >= 1000:
    discount = total_bill * 0.10
elif total_bill >= 500:
    discount = total_bill * 0.05
else:
    pass

final_bill = total_bill - discount

print("==========================================")
print("\tSHOPPING BILL GENERATOR")
print("==========================================")
print()
print("Customer:", customer_name.title())
print()
print("Rice   :" + str(rice_qty) +  " kg"  " =" + " ₹" + str(rice_total))
print("Sugar  :" + str(sugar_qty) + " kg"  " =" + " ₹" + str(sugar_total))
print("Milk   :" + str(milk_qty) +  " kg"  " =" + " ₹" + str(milk_total))
print("Bread  :" + str(bread_qty) + " kg"  " =" + " ₹" + str(bread_total))
print("Eggs   :" + str(eggs_qty) +  " kg"  " =" + " ₹" + str(eggs_total))
print()
print("-------------------------------------------")
print("Total Bill   : " + " ₹" + str(total_bill))
print("Discount     : " + " ₹" + str(round(discount, 2)))
print("Final Bill   : " + " ₹" + str(round(final_bill, 2)))
print("-------------------------------------------")
print()
print("Thank You!")
print("Visit Again")
print()