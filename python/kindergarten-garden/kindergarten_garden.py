PLANT = {"G":"Grass", "C":"Clover", "R":"Radishes", "V":"Violets"}
STUDENT_LIST = ["Alice" ,"Bob" ,"Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]
class Garden:
    def __init__(self, diagram,students=STUDENT_LIST):
        self.diagram = diagram.split('\n')
        self.students = sorted(students)
        self.first_row = self.diagram[0]
        self.second_row = self.diagram[1]

    def plants(self, student):
        s_index = self.students.index(student)
        f_row = [PLANT[i] for i in self.first_row[s_index*2:s_index*2+2]]
        s_row = [PLANT[i] for i in self.second_row[s_index*2:s_index*2+2]]
        return f_row+s_row 