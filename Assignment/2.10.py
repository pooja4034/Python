n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))


def find_product(num1, num2, num3):
    product = 0
    if num1 != 7 and num2 != 7 and num3 != 7:
        product = num1 * num2 * num3
    elif num1 == 7:
        product = num2 * num3
    elif num2 == 7:
        product = num3
    elif num3 == 7:
        product = -1
    return product


final_product = find_product(n1, n2, n3)
print(final_product)