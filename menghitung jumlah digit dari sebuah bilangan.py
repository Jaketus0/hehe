def sum_of_digits(n):
    # Convert integer to string
    str_n = str(n)
    # Split string into individual characters
    digits = [int(digit) for digit in str_n]
    # Sum up the integers
    return sum(digits)
# Example input = 5435
input_number = 5435
print("Sum of digits:", sum_of_digits(input_number))# Output: 17