import spacy
nlp = spacy.load('en_core_web_sm')

gardenpathSentences = ["Time flies like an arrow; fruit flies like a banana", 
                       "Fat people eat accumulates", 
                       "Mary gave the child a Band-Aid", 
                       "That Jill is never here hurts", 
                       "The cotton clothing is made of grows in Mississippi"]

#tokenising sentence with .orth method, then performing named entity recognition using the .ents method 

time = nlp(gardenpathSentences[0])
[token.orth_ for token in time]
print([(token, token.orth_, token.orth) for token in time])
print([(i, i.label_, i.label) for i in time.ents])


fat= nlp(gardenpathSentences[1])
[token.orth_ for token in fat]
print([(token, token.orth_, token.orth) for token in fat])
print([(i, i.label_, i.label) for i in fat.ents])

mary = nlp(gardenpathSentences[2])
[token.orth_ for token in mary]
print([(token, token.orth_, token.orth) for token in mary])
print([(i, i.label_, i.label) for i in mary.ents])

jill = nlp(gardenpathSentences[3])
[token.orth_ for token in jill]
print([(token, token.orth_, token.orth) for token in jill])
print([(i, i.label_, i.label) for i in jill.ents])

cotton = nlp(gardenpathSentences[4])
[token.orth_ for token in cotton]
print([(token, token.orth_, token.orth) for token in cotton])
print([(i, i.label_, i.label) for i in cotton.ents])

#explanation of entities 
gpe = spacy.explain("GPE")
print(f"GPE:{gpe}")

person = spacy.explain("PERSON")
print(f"PERSON:{person}")

#Entity 1: "GPE" = countries, cities, states, in keeping with the word Mississipi 
#Entity 2: "PERSON" = people, including fictional, in keeping with the word "Jill' and "Mary"


