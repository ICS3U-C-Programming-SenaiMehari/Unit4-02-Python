def calculate_factorial(num):
    factorial = 1
    while num > 1:
        factorial *= num
        num -= 1
    return factorial


while True:
    try:
        user_input = int(input("Enter a whole number to calculate its factorial: "))
        if user_input < 0:
            print("Please enter a non-negative number.")
            continue
        elif user_input == 0:
            print("0! = 1")
        else:
            result = calculate_factorial(user_input)
            print(f"{user_input}! = {result}")
        break  # Break out of the loop if input is valid and factorial is calculated
    except ValueError:
        print("Invalid input. Please enter a valid whole number.")
