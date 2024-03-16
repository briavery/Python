def main():
    character = (input("Enter a character: "))

    while len(character) != 1:
        print("Please enter exactly one character. \n Enter input until it is a single char")
        character = (input("Enter a character: "))

    asciiValue = ord(character)

    print(asciiValue)


main()