a = int(input("Enter your age: "))

# Start of if statement number 1

if(a%2==0):
    print("number is even. ")

# End of statment number 1

# Start of If statement number 2

if(a>=18):
    print("You are above the age of consent. ") # the space at the start is called indenattion.
    print("Good for you. ")

elif(a<0):
    print("You are entering an invalid age. ")

elif(a==0):
    print("You are entering 0. ")    

else:
    print("You are below the age of consent. ")    

# End of if statement number 2

print("End of program!!")