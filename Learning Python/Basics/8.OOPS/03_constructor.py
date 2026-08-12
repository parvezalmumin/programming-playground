class Student:

   def __init__(self, fullname):
      self.name = fullname
      print("adding new student in Database...")


s1 = Student("Mumin")
print(s1.name)