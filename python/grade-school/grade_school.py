class School:
    def __init__(self):
        self.students = []

    def add_student(self, name, grade):
        self.students.append({"name":name, "grade": grade})

    def roster(self):
        return [student['name'] for student in sorted(self.students, key = lambda i: (i['grade'], i['name']))]

    def grade(self, grade_number): 
        return [student['name'] for student in sorted([ s for s in self.students if grade_number == s['grade'] ], key=lambda i: i['name'])]