a = input("Enter number 1: ")
b = input("Enter number 2: ")
c = input("Enter number 3: ")
d = input("Enter number 4: ")

greatest = a

if b > greatest:
    greatest = b
if c > greatest:
    greatest = c
if d > greatest:
    greatest = d

print("Greatest number is: ", greatest)           