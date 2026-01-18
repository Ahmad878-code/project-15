def cube(number):
    return number * number * number

def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False

number = int(input("Enter a number: "))

answer = by_three(number)

if answer == False:
    print("Number is not divisible by 3")
else:
    print("Cube is:", answer)
