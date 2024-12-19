class Course:
  def __init__(self, name, unit, grade):
    grade_map = {
      'A': 5,
      'B': 4,
      'C': 3,
      'D': 2,
      'E': 1,
      'F': 0,
    }

    self.grade = grade_map[grade]
    self.name = name
    self.unit = unit

class Semester: 
  def __init__(self, courses):
    self.courses = courses

  def get_total_grade_point(self):
    total = 0
    
    for course in self.courses:
      total += (course.grade * course.unit)
    
    return total
  
  def get_total_units(self):
    total = 0

    for course in self.courses:
      total += course.unit
    
    return total
  
  def compute_gpa(self):
    gpa = self.get_total_grade_point() / self.get_total_units()
    return round(gpa, ndigits=2)

class Results:
  def __init__(self, semesters):
    self.semesters = semesters

  def compute_cgpa(self):
    total_grade_point = 0
    total_units = 0

    for s in self.semesters:
      total_grade_point += s.get_total_grade_point()
      total_units += s.get_total_units()

    cgpa = total_grade_point / total_units
    return round(cgpa, ndigits=2)

session_1_1_courses = [
  Course('COS 101', 3, 'B'),
  Course('COS 141', 3, 'E'),
  Course('GSP 101', 2, 'C'),
  Course('GSP 111', 2, 'B'),
  Course('MTH 111', 3, 'A'),
  Course('MTH 121', 3, 'A'),
  Course('PHY 115', 2, 'A'),
]
session_1_2_courses = [
  Course('COS 102B', 3, 'A'),
  Course('COS 124', 3, 'B'),
  Course('GSP 102', 2, 'C'),
  Course('MTH 122', 3, 'A'),
  Course('MTH 132', 3, 'B'),
  Course('PHY 116', 2, 'A'),
  Course('PHY 118', 2, 'A'),
]
session_2_1_courses = [
  Course('COS 235', 2, 'A'),
  Course('COS 243', 2, 'A'),
  Course('COS 261', 2, 'A'),
  Course('COS 265', 2, 'A'),
  Course('COS 271', 2, 'A'),
  Course('GSP 201', 2, 'B'),
  Course('GSP 207', 2, 'B'),
  Course('MTH 211', 3, 'A'),
  Course('PHY 191', 2, 'A'),
  Course('PHY 351', 2, 'A'),
  Course('STA 131', 2, 'A'),
]
session_2_2_courses = [
  Course('COS 236', 2, 'B'),
  Course('COS 264', 2, 'A'),
  Course('COS 232', 2, 'B'),
  Course('COS 234', 2, 'C'),
  Course('MTH 242', 3, 'A'),
  Course('GSP 202', 2, 'A'),
  Course('GSP 208', 2, 'C'),
  Course('MTH 222', 3, 'C'),
  Course('STA 206', 2, 'A'),
]
session_3_1_courses = [
  Course('COS 335', 2, 'A'),
  Course('COS 341', 2, 'A'),
  Course('CED 341', 2, 'A'),
  Course('COS 361', 3, 'A'),
  Course('COS 331', 2, 'A'),
  Course('COS 313', 3, 'A'),
  Course('COS 333', 2, 'A'),
  Course('COS 311', 2, 'A'),
  Course('COS 337', 2, 'A'),
]

semesters = [
  Semester(session_1_1_courses),
  Semester(session_1_2_courses),
  Semester(session_2_1_courses),
  Semester(session_2_2_courses),
  Semester(session_3_1_courses),
]

results = Results(semesters)

for s in semesters:
  print(s.compute_gpa())
print("----------")
print(results.compute_cgpa())