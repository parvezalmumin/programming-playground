# Search if the word "learning" exists in the file or not. 

with open("Learning Python\\Practice Questions\\practice.txt", "r") as f:
    data = f.read()

if "learning" in data:
    print("The word 'learning' exists in the file.")
else:
    print("The word 'learning' does not exist in the file.")