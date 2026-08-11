""" Write a program to enter 3 subjects from the user and store them in a dictionar. Start with an empty dictionary & add one by one. Use subject name as key & makrs as value """
 

marks = {}

x = int(input("enter phy : "))
marks.update({"phy" : x})

x = int(input("enter chem : "))
marks.update({"chem" : x})

x = int(input("enter math : "))
marks.update({"math" : x})

x = int(input("enter bio : "))
marks.update({"bio" : x})

print(marks)
