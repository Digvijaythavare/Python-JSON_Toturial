import json

FILE = "users.json"


def load_data():
    try:
        with open(FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_data(users):
    with open(FILE, "w") as file:
        json.dump(users, file, indent=4)


def add_user():
    users = load_data()

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    city = input("Enter city: ")

    user = {
        "id": len(users) + 1,
        "name": name,
        "age": age,
        "city": city
    }

    users.append(user)
    save_data(users)

    print("User added successfully!")


def view_users():
    users = load_data()

    if not users:
        print("No users found.")
        return

    for user in users:
        print("\nID:", user["id"])
        print("Name:", user["name"])
        print("Age:", user["age"])
        print("City:", user["city"])


def search_user():
    users = load_data()

    name = input("Enter name to search: ")

    for user in users:
        if user["name"].lower() == name.lower():
            print("\nUser found!")
            print(user)
            return

    print("User not found.")


while True:

    print("\n===== USER MANAGEMENT =====")
    print("1. Add User")
    print("2. View Users")
    print("3. Search User")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_user()

    elif choice == "2":
        view_users()

    elif choice == "3":
        search_user()

    elif choice == "4":
        print("Program closed.")
        break

    else:
        print("Invalid choice!")