class InvalidInputError(Exception):

    def __init__(self, input_value):
        self.input_value = input_value
        super().__init__(f"Invalid input: '{input_value}' is not a valid number.")

def valid_number():
    while True:
        try:
            user_input = input("Please enter a number: ")
            number = float(user_input)
        except ValueError:
            raise InvalidInputError(user_input)
        else:
            print("Input is a valid number.")
            return number
        finally:
            print("End of Program.")

try:
    number = valid_number()
except InvalidInputError as e:
    print(e)