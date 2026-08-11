f = open(r"E:\Programming Playground\Learning Python\Basics\7. File Input-Output\sample.txt", "r+") 
# In sample.txt file - there is "Hi, I am Mumin"
f.write("Hello")
  # It will overwrite   print Hello instead of Hi
print(f.read())
f.close()