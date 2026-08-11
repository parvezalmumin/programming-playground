# Write a recursion function to print all elements in a list
#  Hint: Use list & index as parameter

def print_list(list, idx = 0):
  if(idx == len(list)):
     return
  print(list[idx])
  print_list(list, idx + 1)

fruits = [ "aam", "jaam","kathal", "lichu" ]
print_list(fruits)  
  