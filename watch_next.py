import spacy
nlp = spacy.load('en_core_web_md')

#read in movie.txt file, saved as an array in 'lines'
with open('movies.txt') as f:
    movies = f.readlines()

# description of the hulk movie 
hulk = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."

#function, taking in parameter of any movie description 
def movie_recommendation(desc):
    desc_nlp = nlp(desc) #tokenising movie description 
    best_match = 0.0 
    best_movie = ""
    # iterate through each movie in the txt file, comparing each to the input parameter 
    for movie in movies:
        movie_nlp = nlp(movie) #tokenising each movie line 
        sim = movie_nlp.similarity(desc_nlp) #calculating silmilariy between each line and input parameter and saving to variable 'sim'
        if sim > best_match: #updating best_match and best_movie with the highest similarity result 
            best_match = sim
            best_movie = movie
    return best_movie

#calling function with parameter 'hulk'
next_movie = movie_recommendation(hulk)
print(f" Next recommended movie: {next_movie}")


