try:
    number1 = int(input("Please enter a number: ")) #input 1st number, converted to integer
    operation = input("Please enter an operator (+,-,x,/): ") # input operator
    number2 = int(input("Please enter a number: ")) #input 2nd number 

    if operation == "+": 
        result = number1 + number2 #if operation = +, add 2 numbers
    elif operation == "-":
        result = number1 - number2 #if operation = -, subtract 2nd number from 1st number
    elif operation == "x":
        result = number1 * number2 #if operation = x, multiply 2 numbers
    elif operation == "/":
        result = number1/number2 #if operation = /, divide 1st number by 2nd number
    else:
        print("invalid operation") #if anything other than +,-,x,/ inputed for operation, print error message
except Exception: #if errors encountered such as anything other than numbers inputed, or invalid actions such as divide by 0, print error message
    print("Error, please try again")

# print full equation with result 
print(f"{number1} {operation} {number2} = {result}")

#Writing eqation into a text file
try:
    with open("equations.txt", "a") as f: #open file to append 
        f.write(f"\n{number1} {operation} {number2} = {result}") #add equation to text file, on a new line
except FileNotFoundError as error:
    print("File does not exist") #if file not found error, print message and details of error
    print(error)
finally:
    f.file.close() #close file


 
 

