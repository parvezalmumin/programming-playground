# Write a program to print the elements of a list in a single line. (list is the parameter )

def print_list(lst):
    for item in lst:
        print(item, end=" ")

numbers = [10, 20, 30, 40, 50]
print_list(numbers)