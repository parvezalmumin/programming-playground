# Search for a String
fruits = ("Apple", "Banana", "Mango", "Orange", "Grapes")

x = "Orange"
i = 0

while i < len(fruits):
    if fruits[i] == x:
        print("Found at index", i)
        break
    i += 1
else:
    print("Not Found")