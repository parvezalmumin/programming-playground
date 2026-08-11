nums = (10, 20, 30, 40, 50, 60)

x = 100
i = 0

while i < len(nums):
    if nums[i] == x:
        print("Found at index", i)
        break
    i += 1
else:
    print("Not Found")