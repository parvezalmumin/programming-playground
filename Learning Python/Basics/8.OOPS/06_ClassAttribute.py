class Student:
    school = "ABC School"   # Class attribute

s1 = Student()
s2 = Student()

print(s1.school)
print(s2.school)



        #       Student CLASS
        #            |
        #     school = "ABC School"
        #            |
        #   ┌────────┴────────┐
        #   ↓                 ↓
        # s1 object          s2 object


# When to use class attributes?

# Use them when the value is common/shared among all objects.