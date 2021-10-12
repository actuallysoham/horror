import spacy
import os
import collections

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")


# Get the list of all files and directories
# in the root directory
path = "corpora/shelley"
dir_list = os.listdir(path)

#file_reader = open(path+"/"+dir_list[0],"r")
#file_reader = open(path+"/test.txt","r")
file_reader = open(path+"/Shelley_Mary_1818_Frankenstein.txt","r")

text_shelley = file_reader.read()
#print(text_shelley)

# Process whole documents
text = "Mr Cook and Mrs Shelley from Apple is looking at buying U.K. startup from Dicksbury Johnson for $1 billion"
doc = nlp(text_shelley)

# Analyze syntax
#print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
#print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
print(type(doc.ents))

characters = []
for entity in doc.ents:
    if entity.label_ == 'PERSON':
        print(entity.text, entity.label_)
        characters.append(entity.text)

character_freq = collections.Counter(characters)
print(character_freq)