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
