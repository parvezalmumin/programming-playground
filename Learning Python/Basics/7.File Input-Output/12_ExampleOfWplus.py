f = open(r"E:\Programming Playground\Learning Python\Basics\7. File Input-Output\sample02.txt", "w+") 

# In sample.txt file - there is  written "Hi", And it will be erased because we used w+

print(f.read())
f.close()