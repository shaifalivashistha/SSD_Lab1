ENROLLED_COURSES = {
    "CS2021001": ["Data Structures", "Operating Systems", "Database Systems"],
    "CS2021002": ["Web Development", "Computer Networks"],
}

ATTENDANCE = {
    "CS2021001": 87,
    "CS2021002": 92,
}

def show_dashboard(roll_number):
    courses = ENROLLED_COURSES.get(roll_number)
    if not courses:
        print("No courses found for this student.")
        return None
    print("Enrolled Courses:")
    for course in courses:
        print(f"  - {course}")
    attendance = ATTENDANCE.get(roll_number, 0)
    print(f"Overall Attendance: {attendance}%")
    return courses

def check_attendance_warning(roll_number):
    attendance = ATTENDANCE.get(roll_number, 0)
    if attendance < 75:
        print("Warning: Your attendance is below the required 75% threshold.")
        return True
    return False

GRADES = {
    "CS2021001": {"Data Structures": "A", "Operating Systems": "B+", "Database Systems": "A-"},
    "CS2021002": {"Web Development": "A", "Computer Networks": "B"},
}

def show_grades(roll_number):
    grades = GRADES.get(roll_number)
    if not grades:
        print("No grades available yet.")
        return None
    print("Grades:")
    for course, grade in grades.items():
        print(f"  {course}: {grade}")
    return grades
# TODO: add course registration feature
