# Object Attribute / Instance Attribute : 

# An object attribute (usually called an instance attribute) belongs to a specific object.

class Student:
    school = "ABC School"       # Class attribute

    def __init__(self, name, age):
        self.name = name        # Object attribute
        self.age = age          # Object attribute

s1 = Student("Mumin", 21)
s2 = Student("Karan", 20)

print(s1.name)
print(s2.name)


# Here:

# self.name = name
# self.age = age

# are object/instance attributes.

# Because each object can have different values.

# Student class
# │
# ├── school = "ABC School"  ← Class attribute
# │
# ├── s1
# │   ├── name = "Mumin"     ← Object attribute
# │   └── age = 21           ← Object attribute
# │
# └── s2
#     ├── name = "Karan"     ← Object attribute
#     └── age = 20           ← Object attribute



