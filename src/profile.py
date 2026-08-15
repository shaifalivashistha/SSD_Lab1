
STUDENT_PROFILES = {
    "CS2021001": {"name": "Aarav Sharma", "department": "Computer Science", "year": 3, "email": "aarav@college.edu"},
    "CS2021002": {"name": "Meera Iyer", "department": "Computer Science", "year": 2, "email": "meera@college.edu"},
}

def view_profile(roll_number):
    profile = STUDENT_PROFILES.get(roll_number)
    if not profile:
        print("Profile not found.")
        return None
    print(f"Name: {profile['name']}")
    print(f"Department: {profile['department']}")
    print(f"Year: {profile['year']}")
    print(f"Email: {profile['email']}")
    return profile

def edit_profile(roll_number, field, new_value):
    profile = STUDENT_PROFILES.get(roll_number)
    if not profile:
        print("Profile not found.")
        return False
    if field not in profile:
        print(f"Invalid field: {field}")
        return False
    if field == "email" and "@" not in new_value:
        print("Invalid email format.")
        return False
    profile[field] = new_value
    print(f"Updated {field} to {new_value}.")
    return True

# TODO: add profile picture upload

