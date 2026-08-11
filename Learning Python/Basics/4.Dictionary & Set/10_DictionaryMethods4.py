student = {
    "name" : "mumin",
    "marks" : {
    "java"  : "failed",
    "c"     : 40,
    "c++"   : 44,
    "c"     : 37
    }
}

print(student.items())
print(list(student.items()))

pairs = list(student.items())
print(pairs[0])
print(pairs[1])