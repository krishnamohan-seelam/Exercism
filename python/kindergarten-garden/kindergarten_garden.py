
def chunks(l, n):
    # For item i in a range that is a length of l,
    for i in range(0, len(l), n):
        # Create an index range for l of n items:
        yield l[i:i+n]

class Garden(object):
    default_students =['Alice', 'Bob', 'Charlie', 'David',
                       'Eve', 'Fred', 'Ginny', 'Harriet',
                       'Ileana', 'Joseph', 'Kincaid', 'Larry']
    plant_names =  {'G':'Grass', 'C':'Clover',
                    'R': 'Radishes', 'V': 'Violets'}

    def __init__(self, diagram, students=None):
        self.top,self.bottom  = diagram.split("\n")
        self.students = sorted(students) if students is not None else self.default_students
        self.toprow = list(chunks(self.top,2))
        self.bottomrow = list(chunks(self.bottom,2))
        self.joined_top_bottom = [ top+bottom for top,bottom in zip(self.toprow ,self.bottomrow)]
        self.students_plants = dict(zip(self.students,self.joined_top_bottom))

    def plants(self,student_name):
        plants = self.students_plants[student_name]
        plants= [self.plant_names[plant] for plant in plants]
        return plants 