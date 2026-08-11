# Write a program to the greatest four numbers enteres by the user

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))
d = int(input("Enter Fourth Number: "))

if(a>=b and a>=c and a>=d):
    print("First Number is Largest")
elif(b>=a and b>=c and b>=d):
    print("Second Number is Largest")
elif(c>=a and c>=b and c>=d):
    print("Third Number is Largest")
else:
    print("Fourth Number is Largest")            