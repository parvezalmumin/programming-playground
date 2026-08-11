student = {
    "name" : "mumin",
    "marks" : {
    "java"  : "failed",
    "c"     : 40,
    "c++"   : 44,
    "c"     : 37
    }
}

student.update({"id" : "321456"})

new_dict = {"batch" : "61"}
student.update(new_dict)

new_dict1 = {"age" : "23", "surname" : "pramanik"}
student.update(new_dict1)

print(student)
