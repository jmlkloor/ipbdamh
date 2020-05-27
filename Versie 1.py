import pandas as pd
import re
import nltk.corpus
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
import spacy
import numpy as np
from sklearn import feature_extraction, linear_model, model_selection, preprocessing,svm,tree
from sklearn.naive_bayes import GaussianNB,MultinomialNB,ComplementNB,BernoulliNB,CategoricalNB


nlp = spacy.load('en')
stop = stopwords.words('english')


test_df = pd.read_csv(r"C:\Users\Kevin\Desktop\test.csv",low_memory=False)
train_data = pd.read_csv(r"C:\Users\Kevin\Desktop\train.csv", low_memory=False)

pd.set_option('display.max_colwidth', -1)

cols_to_drop = ['id', 'keyword', 'location']

train_data = train_data.drop(cols_to_drop, axis=1)

print(train_data.head())

print("----------------------------------------------------------------------")

train_data['text'] = train_data['text'].str.lower()
train_data['text'] = train_data['text'].apply(lambda elem: re.sub(r"(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", "", elem))
train_data['text'] = train_data['text'].apply(lambda elem: re.sub(r"\d+", "", elem))

print(train_data.head())

train_data['text'] = train_data['text'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))

print(train_data.head())


#train_data['text'] = train_data['text'].apply(lambda x: word_tokenize(x))

#print(train_data.head())


#def word_stemmer(text):
#    stem_text = [PorterStemmer().stem(i) for i in text]
#    return stem_text

#train_data['text'] = train_data['text'].apply(lambda x: word_stemmer(x))

#print(train_data.head())


#def word_lemmatizer(text):
#    lem_text = [WordNetLemmatizer().lemmatize(i) for i in text]
#    return lem_text

#train_data['text'] = train_data['text'].apply(lambda x: word_lemmatizer(x))

#print(train_data.head())


#def word_pos_tagger(text):
#    pos_tagged_text = nltk.pos_tag(text)
#    return pos_tagged_text

#train_data['text'] = train_data['text'].apply(lambda x: word_pos_tagger(x))

#print(train_data.head())


#text = nlp("forest fire near la ronge sask canada")
#text = nlp("deeds reason earthquake may allah forgive us")
#for chunk in text.noun_chunks:
#    print(chunk.text, chunk.label_, chunk.root.text)


count_vectorizer = feature_extraction.text.CountVectorizer()

train_vectors = count_vectorizer.fit_transform(train_data["text"])

test_vectors = count_vectorizer.transform(test_df["text"])

#gebruik van linear model
#clf = linear_model.RidgeClassifier()

#gebruik van een support vector machine
#clf = svm.SVC()

#decisiontree
#clf = tree.DecisionTreeClassifier()

#Multinomial Naive Bayes
#De beste tot nu toe score = 0.66,0.64.0.71
clf = MultinomialNB()

#Complement naive Bayes
# net iets slechter dan multinomial
#clf = ComplementNB()

#Bernoulli Naive bayes
#score = 0.64,0.60,0.73
#clf = BernoulliNB()

scores = model_selection.cross_val_score(clf, train_vectors, train_data["target"], cv=3, scoring="f1")
print(scores)

