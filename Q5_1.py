# Write an object-oriented program to demonstrate use of default and parameterized constructor.

class Student:
    def __init__(self):
        self.roll_num = 38
        self.name = "Aniket"
        print('Default Constructor :- ', self.roll_num, self.name)

    def display(self, subj, marks):
        self.subj = subj
        self.marks = marks
        print('Parameterized Constructor :- ', self.subj, self.marks)


st = Student()
st.display('Maths', 98)
