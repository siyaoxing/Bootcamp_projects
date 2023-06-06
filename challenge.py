def add_un(word): #1. Function to return a word with the prefix 'un' added 
    return print ('un'+word)

add_un('happy')

vocab_words = ['prefix', 'word', "word2"] #2. Function to return the same prefix to a group of words 

def make_word_groups(vocab_words):
    i=1
    while i<len(vocab_words):
        new = print(vocab_words[0]+vocab_words[i])
        i+=1
    return new 

make_word_groups(vocab_words) #3. Function to remove the suffix 'ness' and return the original word

def remove_suffix_ness(word):
    if word[-5:] =='iness':
        return print (word.replace('iness', 'y'))
    else:
        return print(word.replace('ness', ''))
    

remove_suffix_ness('handsomeness')

def adjective_to_verb(sentence, index): #4. Function to make any adjective in a sentence into a verb
    new_sentence = sentence.split(" ")
    return print(new_sentence[index]+'en')

adjective_to_verb('It is too bright', -1)
        
