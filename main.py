def sum_of_digits(number):
    # Ensure the number is positive
    number = abs(number)
    total = 0

    # Calculate the sum of digits
    while number > 0:
        total += number % 10  # Add the last digit
        number //= 10  # Remove the last digit

    return total

# Test the function
num = int(input("Enter a number: "))

print("The sum of digits is:", sum_of_digits(num))
