# Simple Login Authentication System

# Store user data in a dictionary (username: password)
user_data = {}

def register():
    print("\n=== Register ===")
    username = input("Enter a new username: ")
    if username in user_data:
        print("Username already exists! Please try a different one.")
        return
    password = input("Enter a new password: ")
    user_data[username] = password
    print("Registration successful! You can now login.")

def login():
    print("\n=== Login ===")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if user_data.get(username) == password:
        print(f"Welcome, {username}! You've successfully logged in.")
        secured_page(username)
    else:
        print("Invalid username or password. Please try again.")

def secured_page(username):
    print("\n=== Secured Page ===")
    print(f"Hello {username}, you have accessed the secured page.")
    while True:
        choice = input("Enter 'logout' to log out: ").strip().lower()
        if choice == 'logout':
            print("You've been logged out successfully.")
            break

def main():
    while True:
        print("\n=== Main Menu ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
