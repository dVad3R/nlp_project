# pip install -U pip
# pip install spacy
# python -m spacy download en_core_web_sm
# https://spacy.io/

import spacy

# load txt with our story
story = open("../resources/story.txt", "r").read()

#print(story)

# load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")

# parse story into the nlp
story_processed = nlp(story)

# list that will store all nouns inside the story
nouns = [chunk.text for chunk in story_processed.noun_chunks]

# list that will store all verbs inside the story
verbs = [token.lemma_ for token in story_processed if token.pos_ == "VERB"]

# counter for sentences
counter = 0

# iterate through each sentence and print it
for sentence in story_processed.sents:
    # increment by 1
    counter += 1

    # sentences as a list
    list_sentence = sentence.text.replace(",", "").split(" ")

    # print current sentence
    print("[*] Sentence", counter, ":",  sentence.text)
    
print("\n~ The given story contained", counter, "sentences. ~")