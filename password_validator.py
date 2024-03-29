def main():

    password = input("Insert your password: ")
    isUpper = any(i.isupper() for i in password)
    isLower = any(i.islower() for i in password)
    specialCharacter = password.__contains__('!') or password.__contains__('@') or password.__contains__('#') or password.__contains__('$') or password.__contains__('%') or password.__contains__('&') or password.__contains__('*')

    while not(len(password) > 8 and len(password) < 20 and isUpper and isLower and specialCharacter):
        if(len(password) < 8):
            print("Password is too short (8 minimum).")
        elif(len(password) > 20):
            print("Password is too long (20 maximum)")
        elif(not isUpper):
            print("Password does not contain an uppercase.")
        elif(not isLower):
            print("Password does not include a lowercase.")
        elif(not specialCharacter):
            print("Password does not include a special character (!@#$%&*).")

        password = input("Insert a new password: ")
        isUpper = any(i.isupper() for i in password)
        isLower = any(i.islower() for i in password)
        specialCharacter = password.__contains__('!') or password.__contains__('@') or password.__contains__(
            '#') or password.__contains__('$') or password.__contains__('%') or password.__contains__(
            '&') or password.__contains__('*')

    confirm = input("Enter your password in again for confirmation: ")

    if password == confirm:
        print("Password successfully set")
    else:
        print("Passwords do not match. Please restart.")
        main()



main()