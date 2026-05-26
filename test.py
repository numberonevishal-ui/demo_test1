def add_numbers(num1, num2):
    return sum(int(digit) for digit in str(num1 + num2))

num1 = 10
num2 = 20
print(add_numbers(num1, num2))