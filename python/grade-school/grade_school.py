from collections import defaultdict

class School(object):
    def __init__(self):
        self.grades_map = defaultdict(list)

    def add_student(self, name, grade):
        self.grades_map[grade].append(name)

    def roster(self):
        students_roster = []
        for grade_number in sorted(self.grades_map.keys()):
            students_roster += self.grade(grade_number)
        return students_roster

    def grade(self, grade_number):
        return sorted(self.grades_map[grade_number])
