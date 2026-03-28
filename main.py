from password_manager import add_password, view_password, delete_password, list_sites
import random
import string

MASTER_PASSWORD = "admin123"

def generate_password():

    characters = string.ascii_letters + string.digits + "!@#$%&*"

    password = ""

    for i in range(12):
        password += random.choice(characters)

    return password


def login():

    print("CyberSafe Password Manager Login")

    password = input("Enter master password: ")

    if password == MASTER_PASSWORD:
        print("Access granted")
        return True
    else:
        print("Wrong password")
        return False


def menu():

    while True:

        print("\nCyberSafe Password Manager")
        print("1 Add Password")
        print("2 View Password")
        print("3 Delete Password")
        print("4 List Saved Sites")
        print("5 Generate Strong Password")
        print("6 Exit")

        choice = input("Enter choice: ")

        if choice == "1":

            site = input("Enter site name: ")
            username = input("Enter username: ")
            password = input("Enter password: ")

            add_password(site, username, password)

            print("Password stored successfully!")

        elif choice == "2":

            site = input("Enter site name: ")

            result = view_password(site)

            if result:
                username, password = result
                print("Username:", username)
                print("Password:", password)
            else:
                print("No record found")

        elif choice == "3":

            site = input("Enter site name:")

            if delete_password(site):
                print("Record deleted")
            else:
                print("Record not found")

        elif choice == "4":

            sites = list_sites()

            if sites:
                print("Saved sites:")
                for s in sites:
                    print("-", s)
            else:
                print("No saved passwords")

        elif choice == "5":

            new_password = generate_password()

            print("Generated Strong Password:", new_password)

        elif choice == "6":
            break

        else:
            print("Invalid choice")


if login():
    menu()
    
