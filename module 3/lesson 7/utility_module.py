
def percentage(part, total):
    return (part / total) * 100

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def check_grade(mark):
    if mark >= 80:
        return "A+"
    elif mark >= 70:
        return "A"
    elif mark >= 60:
        return "A-"
    else:
        return "Needs Improvement"

def rectangle_area(length, width):
    return length * width
