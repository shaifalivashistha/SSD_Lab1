def show_menu():
    print("\n=== Student Portal ===")
    print("1. Login")
    print("2. View Profile")
    print("3. Dashboard")
    print("4. Settings")
    print("5. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            print("Redirecting to login...")
        elif choice == "2":
            print("Redirecting to profile...")
        elif choice == "3":
            print("Redirecting to dashboard...")
        elif choice == "4":
            print("Redirecting to settings...")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
