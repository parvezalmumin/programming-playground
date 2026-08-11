with open(r"E:\Programming Playground\Learning Python\Basics\7. File Input-Output\sample04.txt", "r") as f:
     data = f.read()
     print(data)


with open(r"E:\Programming Playground\Learning Python\Basics\7. File Input-Output\sample04.txt", "w") as f:
     f.write("New Data")