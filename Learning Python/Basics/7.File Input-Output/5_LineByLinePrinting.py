f = open(r"E:\Programming Playground\Learning Python\Basics\7. File Input-Output\demo.txt", "r")

line1 = f.readline() #Read one Line at a time
print(line1)

line2 = f.readline() #Read one Line at a time
print(line2)

line3 = f.readline() #Read one Line at a time
print(line3) #EMPTY


f.close() 