def square_number():
    try:
        number = input("Enter a number to square: ")
        squared_number = int(number) ** 2
        print(f"The square of {number} is {squared_number}.")
    except ValueError:
        print("Please input a number.")
        square_number()
square_number()
