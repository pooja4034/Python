def calculate_bill_amount(food_type, quantity, distance):
    if food_type != 'V' and food_type != 'N':
        return -1
    if distance <= 0:
        return -1
    if quantity < 1:
        return -1

    veg_combo_cost = 120
    non_veg_combo_cost = 150
    delivery_charge_per_km = 0
    total_cost = 0

    if food_type == 'V':
        total_cost = quantity * veg_combo_cost
    elif food_type == 'N':
        total_cost = quantity * non_veg_combo_cost

    if distance > 0 and distance <= 3:
        delivery_charge_per_km = 0
    elif distance > 3 and distance <= 6:
        delivery_charge_per_km = 3
    elif distance > 6:
        delivery_charge_per_km = 6

    final_bill_amount = total_cost + (delivery_charge_per_km * distance)
    return final_bill_amount

food_type = 'N' 
quantity = 2  
distance = 4  

bill_amount = calculate_bill_amount(food_type, quantity, distance)
if bill_amount == -1:
    print("Invalid input. Please check the provided information.")
else:
    print(f"Final bill amount: Rs. {bill_amount}")