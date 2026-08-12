# the __init__() constructor

class Student:

   def __init__(self, fullname):
      self.name = fullname
      print("adding new student in Database...")


s1 = Student("Mumin")
print(s1.name)

s1 = Student("Parvez")
print(s1.name)



#  ----
# Complete execution
# _____________________

# Student("Mumin")
#        ↓
# __init__(self, fullname)
#        ↓
# fullname = "Mumin"
#        ↓
# self.name = fullname
#        ↓
# s1.name = "Mumin"
#        ↓
# print(s1.name)
#        ↓
# Mumin

# _________________________________

# The key concept to remember

# __init__() → automatically runs when an object is created.

# And:

# self.name → data belonging to that particular object.

