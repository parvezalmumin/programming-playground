f = open(r"E:\Programming Playground\Learning Python\Basics\7. File Input-Output\draft.txt", "a") #This will add new line, it will not remove previous messages

data = f.write("Hehe, Another Line")
print(data)
print(type(data))

f.close()