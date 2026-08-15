STUDENTS = {
    "CS2021001": "pass123",
    "CS2021002": "pass456",
}

def login(roll_number, password):
    if not roll_number or not password:
        print("Roll number and password are required.")
        return False
    print(f"Attempting login for {roll_number}...")
    if STUDENTS.get(roll_number) == password:
        print("Login successful.")
        return True
    print("Invalid roll number or password.")
    return False
