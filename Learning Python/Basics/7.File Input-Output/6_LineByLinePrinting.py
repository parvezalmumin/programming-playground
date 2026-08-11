f = open(r"E:\Programming Playground\Learning Python\Basics\7. File Input-Output\demo.txt", "r")

data = f.read()
print(data)

line1 = f.readline() #Now its Empty
print(line1)

line2 = f.readline() #Now its empty
print(line2)

f.close() 
