# Search for a number X in this tuple using loop:
# ( 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36 )
#This code right version of code 8

nums = ( 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36 )

x = 36
i = 0
while i < len(nums):
  if(nums[i] == x):
    print("Found at idx",i)
    break
  else:
    print("Finding...")  
  i += 1
print("End Of Code")  