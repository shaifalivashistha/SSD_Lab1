STUDENT_SETTINGS = {
    "CS2021001": {"password": "pass123", "phone": "9876543210", "notifications": True},
    "CS2021002": {"password": "pass456", "phone": "9123456789", "notifications": True},
}

def view_settings(roll_number):
    settings = STUDENT_SETTINGS.get(roll_number)
    if not settings:
        print("Settings not found.")
        return None
    print(f"Phone: {settings['phone']}")
    print(f"Notifications: {'On' if settings['notifications'] else 'Off'}")
    return settings

def change_password(roll_number, old_password, new_password):
    settings = STUDENT_SETTINGS.get(roll_number)
    if not settings:
        print("Settings not found.")
        return False
    if settings['password'] != old_password:
        print("Old password is incorrect.")
        return False
    if len(new_password) < 6:
        print("New password must be at least 6 characters.")
        return False
    settings['password'] = new_password
    print("Password updated successfully.")
    return True

def update_phone(roll_number, new_phone):
    settings = STUDENT_SETTINGS.get(roll_number)
    if not settings:
        print("Settings not found.")
        return False
    if not new_phone.isdigit() or len(new_phone) != 10:
        print("Invalid phone number. Must be 10 digits.")
        return False
    settings['phone'] = new_phone
    print("Phone number updated successfully.")
    return True
