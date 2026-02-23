#a = int(input("Enter Maths Marks: "))
#b = int(input("Enter DBMS Marks: "))
#c = int(input("Enter DSA Marks: "))
#
#if a >= 33 :
#    print("Passed in Maths")
#else:
#    print("Failed in Maths")
#
#if b >= 33 :
#    print("Passed in DBMS")
#else:
#    print("Failed in DBMS")
#
#if c >= 33 :
#    print("Passed in DSA")
#else:
#    print("Failed in DSA")
#
#sum = a + b + c
#percentage = sum*100/300
#
#if percentage >= 40:
#    print("Passed....Congratulations!!")
#    
#else :
#    print("Failed....Better luck next time!!")


# if the student fails in one subject still he got max marks in other subjects then he will be passed and this is the main backlash of this code 

# so followint code will work right for the current scenario

sub1 = int(input("Enter marks of subject 1: "))
sub2 = int(input("Enter marks of subject 2: "))
sub3 = int(input("Enter marks of subject 3: "))

total_percentage = (sub1 + sub2 + sub3) / 3

if sub1 >= 33 and sub2 >= 33 and sub3 >= 33 and total_percentage >= 40:
    print("Congratulations! You Passed.")
else:
    print("Sorry, You Failed.")



       



