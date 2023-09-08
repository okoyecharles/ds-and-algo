# Practicing lambdas and higher order functions

students = [
    ['Charles', 20, 'High School'],
    ['Ally', 19, 'High School'],
    ['Bro', 15, 'Primary School'],
    ['E', 28, 'High School'],
    ['F', 46, 'Middle School'],
    ['G', 92, 'High School'],
    ['H', 23, 'Middle School'],
    ['I', 12, 'High School']
]

def graduate(students):
    next_class = {
        'Primary School': 'Middle School',
        'Middle School': 'High School',
        'High School': 'Graduated'
    }
    students = list(map(lambda student: [student[0], student[1], next_class[student[2]]], students))
    return students

print(graduate(students))