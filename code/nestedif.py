number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
    if number % 2 == 0:
        print("It is an even number.")
    else:
        print("It is an odd number.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")