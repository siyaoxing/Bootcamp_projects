#Changes individual characters to alternate between lower and upper case:


sentence = input("Please enter a word or sentence: ") #user input 
new_sentence = " " #new blank variable to add changes to 

#iterate through each character of user input 
#stops at the last letter, which is the same as the length of the string
for i in range(len(sentence)): 
    if i%2==0: #if i is even number
        new_sentence+=sentence[i].upper() #Change character at index i to upper case and assign to variable new_sentence
    else:
        new_sentence+=sentence[i].lower() #if i is odd, change character at index i to lower case and assign to variable new_sentence
print(new_sentence) #print final sentence



#Changes words to alternate between upper and lower case:


sentence = input("Please enter a word or sentence: ") #user input 
split_sentence = sentence.split() #split user input by space and assign to new variable 
new_sentence2 = " " #blank variable to add changes to 

#iterate through each character of user input 
#stops at the last letter, which is the same as the length of the string
for i in range(len(split_sentence)):
    if i%2==0: #if i is even, change word at index i to uppercase with space after 
        new_sentence2+=f"{split_sentence[i].upper()} "
    else: #if i is odd, change word at index i to lowercase with space after 
        new_sentence2+=f"{split_sentence[i].lower()} "
print(new_sentence2)
