student = {
    "name" : "mumin",
    "marks" : {
    "java"  : "failed",
    "c"     : 40,
    "c++"   : 44,
    "c"     : 37
    }
}

print(student["name"])
print(student.get("name"))

# print(student["name2"])   => this will get error
# print(student.get("name2"))  => this will get none

print(student.get("name2"))