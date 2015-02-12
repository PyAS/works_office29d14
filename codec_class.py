lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

students = [lloyd, alice, tyler]

for names in students:
    for data in names:
        print names[data]

# Add your function below!
def average(numbers):
    return float(sum(numbers)) / len(numbers)

def get_average(student):
    homework = average(student["homework"])
    quizz = average(student["quizzes"])
    test = average(student["tests"])
    print (homework*0.1)+(quizz*0.3)+(test*0.6)

score = get_average(lloyd)
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    else:
        return "F"

get_letter_grade(score)

def get_class_average(student):
    results = []
    for student in students:
        result = get_average(student)
        results.append(result)
    print average(results)

classavg = get_class_average(students)
print classavg
print get_letter_grade(classavg)
