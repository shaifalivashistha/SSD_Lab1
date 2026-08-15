STUDENTS = {
    "CS2021001": "pass123",
    "CS2021002": "pass456",
}

MAX_ATTEMPTS = 3

def login(roll_number, password, attempt=1):
    if not roll_number or not password:
        print("Roll number and password are required.")
        return False
    if attempt > MAX_ATTEMPTS:
        print("Too many failed attempts. Account locked.")
        return False
    print(f"Attempting login for {roll_number}... (attempt {attempt})")
    if STUDENTS.get(roll_number) == password:
        print("Login successful.")
        return True
    print("Invalid roll number or password.")
    return False
