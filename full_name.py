#variable to store name inputed by user
full_name = input("Please enter your full name: ")

# if no characters entered, print statement
if len(full_name) ==0 :
    print("You haven't entered anything. Please enter your full name")

# if more than 25 characters entered, print statement
elif len(full_name) >25:
    print("You have entered more than 25 characters. Please make sure that you have only entered your full name.")

# if less than 4 characters entered, print statement
elif len(full_name)<4:
    print("You have entered less than 4 characters. Please make sure tha you have entered your name and surname.")

# if >4 characters and <25 characters entered, print statement
else:
    print("Thank you for entering your name.")