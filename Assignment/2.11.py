def find_minimum_coins(x, y, z):
    total_amount = (x * 5) + (y * 1)

    if total_amount < z:
        return -1

    five_rupee_coins_needed = min(x, z // 5)
    remaining_amount = z - (five_rupee_coins_needed * 5)
    one_rupee_coins_needed = min(y, remaining_amount)

    return five_rupee_coins_needed, one_rupee_coins_needed
x = 10  
y = 20  
z = 85  

result = find_minimum_coins(x, y, z)
if result == -1:
    print("Exact change is not possible.")
else:
    five_rupee_coins, one_rupee_coins = result
    print(f"Number of 5 rupee coins: {five_rupee_coins}")
    print(f"Number of 1 rupee coins: {one_rupee_coins}")