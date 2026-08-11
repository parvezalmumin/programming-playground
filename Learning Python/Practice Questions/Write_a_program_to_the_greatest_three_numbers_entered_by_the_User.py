# Write a program to the greatest three numbers enteres by the user

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))

if a >= b and a >= c:
    print("First number is greatest")

elif b >= a and b >= c:
    print("Second number is greatest")

else:
    print("Third number is greatest")