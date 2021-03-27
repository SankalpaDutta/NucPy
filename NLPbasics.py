import spacy
import numpy as np

nlp = spacy.load('en_core_web_sm')

doc=nlp(u' Tesla is buying U.A.E. for $6 million')

for token in doc:
    print(token.text,token.pos,token.pos_)


doc2 = nlp(u'This is first sentence. This is second sentence. This is third sentence')


for sentence in doc2.sents:
    print(sentence)

print(doc2[5].is_sent_start)  #returns if the word is starting the sentence "This"



 #Tokenization

 