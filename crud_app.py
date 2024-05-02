def check():
    try:
        file = open("../customer_list.txt", 'r')
        lines = file.readlines()
        file.close()
        return lines
    except FileNotFoundError:
        print("Customer list does not exist. Creating a new file...")
        return []

def create():
    customer = check()
    fname = input("Please enter the customer\'s first name: ")
    lname = input("Please enter the customer\'s last name: ")
    phone = input("Please enter the customer\'s phone: ")
    email = input("Please enter the customer\'s email: ")
    entry = f"{fname}, {lname}, {phone}, {email}\n"
    customer.append(entry)
    save(customer)

def save(output):
    file = open("../customer_list.txt", 'w')
    for line in output:
        file.write(line)
    file.close()
    print("File updated.")

def read():
    customer_list = check()
    last_name = input("Please enter the customer's last name to search: ")
    found = False
    for entry in customer_list:
        fname, lname, phone, email = entry.split(", ")
        if lname.strip() == last_name:
            print(f"First Name: {fname}")
            print(f"Last Name: {lname}")
            print(f"Phone: {phone}")
            print(f"Email: {email}")
            found = True
            break
    if not found:
        print("Entry not found.")

def update():
    customer_list = check()
    last_name = input("Please enter the last name of the customer to update: ")
    updated_customer_list = []
    updated = False
    for entry in customer_list:
        fname, lname, phone, email = entry.split(", ")
        if lname.strip() == last_name:
            print("Enter new information:")
            new_fname = input(f"First Name: ") or fname
            new_lname = input(f"Last Name: ") or lname
            new_phone = input(f"Phone: ") or phone
            new_email = input(f"Email: ") or email
            entry = f"{new_fname}, {new_lname}, {new_phone}, {new_email}\n"
            updated = True
        updated_customer_list.append(entry)
    if updated:
        save(updated_customer_list)
        print("Entry updated successfully.")
    else:
        print("Entry not found.")

def delete():
    customer_list = check()
    last_name = input("Please enter the last name of the customer to delete: ")
    new_customer_list = []
    deleted = False
    for entry in customer_list:
        fname, lname, _, _ = entry.split(", ")
        if lname.strip() != last_name:
            new_customer_list.append(entry)
        else:
            deleted = True
    if deleted:
        save(new_customer_list)
        print("Entry deleted successfully.")
    else:
        print("Entry not found.")
def main_menu():
    print("Menu:")
    while True:
        try:
            print(
                "\nWelcome! You can create new email entries, change email addresses, delete entries, or display entries.")
            print("1. Create a new entry")
            print("2. Display an entry by last name")
            print("3. Update an existing entry")
            print("4. Remove an entry")
            print("5. Quit")
            choice = int(input("Please enter the number of your selection: "))
            if 1 <= choice <= 5:
                if choice == 1:
                    create()
                elif choice == 2:
                    read()
                elif choice == 3:
                    update()
                elif choice == 4:
                    delete()
                elif choice == 5:
                    quit()
            else:
                print("That is not a valid number. Try again.")
        except ValueError:
            print("That is not a valid number. Try again.")

main_menu()