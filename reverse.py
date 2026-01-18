def reverse_num(number):
    reverse_number = 0
    while number > 0:
        digit = number % 10
        reverse_number = (reverse_number * 10) + digit
        number = number // 10
    return reverse_number
number = int(input("Enter a number:"))
print("Reverse number is", reverse_num(number))