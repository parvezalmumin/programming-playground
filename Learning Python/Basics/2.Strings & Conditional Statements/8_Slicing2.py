str = "Parvez Al Mumin"
print(str[-4:-1])
print(str[-6:-1])
print(str[:])  #Whole String
print(str[::2])  #Take every second character.
print(str[::-1]) #Reverse String


text = "python"
print(text.upper())
print(text.lower())


txt = "i love python"
print(txt.title())


text = "   hello   "
print(text.strip())


text = "I like Java"
print(text.replace("Java","Python"))


text = "Programming"
print(text.find("g"))



text = "banana"
print(text.count("a"))



text = "Python"
print(text.startswith("Py"))
print(text.endswith("on"))



sentence = "I love Python"
print(sentence.split())


words = ["I","Love","Python"]
print(" ".join(words))