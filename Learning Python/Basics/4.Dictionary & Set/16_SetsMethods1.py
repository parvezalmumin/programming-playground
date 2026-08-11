collection = set()
collection.add(1)
collection.add(2)
collection.add(2)
collection.add(2)
collection.add(3)
collection.add(4)
collection.add(4)
collection.add("mumin")
collection.add((1,2,3))


print(collection)
print(len(collection))

collection.clear()
print(collection)
print(len(collection))