# Write  A FUNCTION replaces all occurrences of "Java" with "python" in above file. 

with open("Learning Python\Practice Questions\practice.txt", "r") as f:
     data = f.read()

new_data = data.replace("Java", "Python")
print(new_data)     


with open("Learning Python\Practice Questions\practice.txt", "w") as f:
     f.write(new_data)