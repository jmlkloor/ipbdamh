import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.util import bigrams,trigrams,ngrams
from nltk.stem import PorterStemmer
from nltk.stem import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import re
from nltk import ne_chunk

tekst = "Haha South Tampa is getting flooded hah- WAIT A SECOND I LIVE IN SOUTH TAMPA WHAT AM I GONNA DO WHAT AM I GONNA DO FVCK #flooding"
tekst2 = "Forest fire near La Ronge Sask. Canada"

tekst_tokenize = word_tokenize(tekst)

print(tekst_tokenize)

print(len(tekst_tokenize))

fdist = FreqDist()

for word in tekst_tokenize:
    fdist[word.lower()]+=1
print(fdist)

fdist_top10 = fdist.most_common(10)
print(fdist_top10)

quotes_tokens = nltk.word_tokenize(tekst)

quotes_bigrams = list(nltk.bigrams(quotes_tokens))

print(quotes_bigrams)

pst=PorterStemmer()

print(pst.stem("having"))

words_to_stem=["give","giving","given","gave"]
for words in words_to_stem:
    print(words+ ":" +pst.stem(words))

print(".")

word_lem=WordNetLemmatizer()

punctuation=re.compile(r'[#-.?!,:;()|0-9]')

post_punctuation=[]
for words in tekst_tokenize:
    word=punctuation.sub("",words)
    if len(word)>0:
        post_punctuation.append(word)

print(post_punctuation)

sent_tokens = word_tokenize(tekst)

for token in sent_tokens:
    print(nltk.pos_tag([token]))

NE_tokens = word_tokenize(tekst)
NE_tags = nltk.pos_tag(NE_tokens)
NE_NER = ne_chunk(NE_tags)
print(NE_NER)


new_tokens = nltk.pos_tag(word_tokenize(tekst))
print(new_tokens)

print([s for s in new_tokens if s[1] == 'NN' or s[1] == 'NNS' ])

new_tokens2 = nltk.pos_tag(word_tokenize(tekst2))
print(new_tokens2)

print([s for s in new_tokens2 if s[1] == 'NN'])



#grammar_np = r"NP: {<DT>?<JJ>*<NN>}"
#chunk_parser = nltk.RegexpParser(grammar_np)
#chunk_result = chunk_parser.parse(new_tokens)
#print(chunk_result)

