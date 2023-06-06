import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# cat and monkey are the most similar, monkey and banana is less similar, cat and monkey is the least similar 

word4 = nlp('forest')
word5 = nlp('mountain')
word6 = nlp('sky')

print(word4.similarity(word5))
print(word4.similarity(word6))
print(word5.similarity(word6))

nlp = spacy.load('en_core_web_sm')

word4 = nlp('forest')
word5 = nlp('mountain')
word6 = nlp('sky')

print(word4.similarity(word5))
print(word4.similarity(word6))
print(word5.similarity(word6))

# with 'en_core_web_sm', the numbers are a lot higher - 0.77, 0.75, 0.8 vs 0.66, 0.39, 0.37 respectively 

