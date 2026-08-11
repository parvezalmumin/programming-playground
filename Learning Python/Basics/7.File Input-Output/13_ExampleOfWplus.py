f = open(r"E:\Programming Playground\Learning Python\Basics\7. File Input-Output\sample03.txt", "w+") 

# In sample.txt file - there is  written "Hi", And it will be erased because we used w+

print(f.read())

f.write("Hello") # now in text file we can see "Hello"

f.close()