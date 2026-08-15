def login(roll_number, password):
    if not roll_number or not password:
        print("Roll number and password are required.")
        return False
    print(f"Attempting login for {roll_number}...")
    return True
