# variables to keep track of how many numbers have been inputed (counter) and total sum of numbers (total)
counter = 0
total = 0

# ask user to input a number, which is saved to the number variable 
# convert input to float so user can use decimals and whole numbers 
number = float(input("Please enter a number: "))

# While number is equal or greater than 0, execute the indented code below 
# Once a negative number is entered, the loop will stop 
while number >= 0:
    total += number #add number inputed to the total variable 
    print(total) #print the new sum of inputed numbers
    counter +=1 # adds 1 to the counter variable each time a number is inputed, so we can calculate the average at the end 
    print(counter) #print counter variable, which is how many numbers have been inputed 
    number = float(input("Please enter a number: ")) #asks user to input anothe number while the while condition is true

#average = sum of all numbers (total) divided by number of numbers (counter)
average = total/counter
print("Average: "+str(average)) 