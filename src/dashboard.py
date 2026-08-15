ENROLLED_COURSES = {
    "CS2021001": ["Data Structures", "Operating Systems", "Database Systems"],
    "CS2021002": ["Web Development", "Computer Networks"],
}

def show_dashboard(roll_number):
    courses = ENROLLED_COURSES.get(roll_number)
    if not courses:
        print("No courses found for this student.")
        return None
    print("Enrolled Courses:")
    for course in courses:
        print(f"  - {course}")
    return courses
