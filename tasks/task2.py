# pip install --user -U nltk

import nltk
from nltk import text
import spacy

grammar = nltk.CFG.fromstring(""" 
S -> NP VP 
NP -> PN | Det N | N 
VP -> IV | IV ADV | AV ADJ | TV PN NP | V NP 
Det -> 'the' | 'a' | 'an' 
ADJ -> 'scary' | 'tall' | 'short' | 'blonde' | 'slim' | 'fat' 
N -> 'cat' | 'dog' | 'cats' | 'food' | 'book'| 'books'
AV -> 'is' | 'does' | 'are' | 'do' 
IV -> 'runs' | 'run' | 'running' | 'hurts' | 'hurt' | 'hurting' | 'walks' | 'walk' | 'walking' | 'jumps' | 'jump' | 'jumping' | 'shoots' | 'shoot' | 'shooting' 
TV -> 'gives' | 'give' | 'gave' | 'giving' 
V -> 'chased' | 'chase' | 'needs' | 'need' | 'hates' | 'hate' | 'has' | 'have' | 'loves' | 'love' | 'kicks' | 'kick' | 'jumps' | 'jump' 
PN -> 'Mary' | 'John' | 'Tommy' 
ADV -> 'quickly' | 'slowly' | 'independently' """)

# store dog.txt as a string
dog_txt = open("../resources/dog.txt", "r").read()

# store mary.txt as a string
mary_txt = open("../resources/mary.txt", "r").read()

# load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")


parser = nltk.ChartParser(grammar) 



text_file = ""

try: 
    text_selection = int(input("[*] Please select a text file (1 or 2).\n"))

    if text_selection == 1:
        text_file = dog_txt
    elif text_selection == 2:
        text_file = mary_txt
    else:
        print("Invalid input. Selecting default text file...")
        text_file = dog_txt
except:
    print("Invalid input. Selecting default text file.")
    text_file = dog_txt

for sentence in nlp(text_file).sents:

    # print current sentence
    sent = sentence.text.replace(".","").split(" ")

    for tree in parser.parse(sent):
        tree.draw()