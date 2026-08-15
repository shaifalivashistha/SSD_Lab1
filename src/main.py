from login import login
from profile import view_profile
from dashboard import show_dashboard, check_attendance_warning, show_grades
from settings import view_settings, change_password, update_phone, toggle_notifications

def show_menu():
    print("\n=== Welcome to Student Portal ===")
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
            roll = input("Roll number: ")
            pwd = input("Password: ")
            login(roll, pwd)
        elif choice == "2":
            roll = input("Enter roll number: ")
            view_profile(roll)
        elif choice == "3":
            roll = input("Enter roll number: ")
            show_dashboard(roll)
            check_attendance_warning(roll)
            show_grades(roll)
        elif choice == "4":
            roll = input("Enter roll number: ")
            view_settings(roll)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
