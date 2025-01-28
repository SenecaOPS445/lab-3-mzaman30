def square(number):
    return number ** 2

def sum_numbers(number1, number2):
    return int(number1) + int(number2)

# Testing the square function
print(square(5))  # 25
print(square(10))  # 100
print(square(12))  # 144
print(square(square(2)))  # 16 (square of 4)

# Testing the sum_numbers function
print(sum_numbers(5, 10))  # 15
print(sum_numbers(50, 100))  # 150
print(square(sum_numbers(5, 5)))  # 100 (square of 10)
