def calculate_max_number(num1, num2):
    if num1 >= num2:
        return -1

    numbers = []

    for num in range(num1, num2 + 1):
        if sum_of_digits(num) % 3 == 0 and is_two_digit_number(num) and num % 5 == 0:
            numbers.append(num)

    if not numbers:
        return -1

    return max(numbers)


def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))


def is_two_digit_number(number):
    return 10 <= number <= 99


# Example usage:
num1 = 10
num2 = 100

result = calculate_max_number(num1, num2)
print("Maximum number:", result)