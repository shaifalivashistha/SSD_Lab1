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
