
class Student:

   def __init__(self, name, marks):
      self.name = name
      self.marks = marks
      print("adding new student in Database...")


s1 = Student("Mumin", 90)
print(s1.name, s1.marks)

s1 = Student("Parvez", 91)
print(s1.name, s1.marks)

