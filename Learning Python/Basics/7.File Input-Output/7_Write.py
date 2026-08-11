f = open(r"E:\Programming Playground\Learning Python\Basics\7. File Input-Output\draft.txt", "w")

# I wrote in text file that these messages woul ne deleted

data = f.write("All the previous messages got deleted. ") # Now, The prevvious messages were deleted and these messages were saved in text file.

print(data) # Why does it print 37? = The write() method returns the number of characters written to the file.

f.close()