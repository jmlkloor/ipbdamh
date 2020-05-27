import pandas as pd
import re
from nltk.corpus import stopwords
import spacy
from sklearn import feature_extraction, linear_model, model_selection, preprocessing,svm,tree
from sklearn.naive_bayes import GaussianNB,MultinomialNB,ComplementNB,BernoulliNB,CategoricalNB

#hier laden wij voor nltk library's in
nlp = spacy.load('en')
stop = stopwords.words('english')

#hier laden wij de data in
test_df = pd.read_csv(r"C:\Users\Kevin\Desktop\test.csv",low_memory=False)
train_data = pd.read_csv(r"C:\Users\Kevin\Desktop\train.csv", low_memory=False)

#hier verwijderen wij kolommen
pd.set_option('display.max_colwidth', -1)
cols_to_drop = ['id', 'keyword', 'location']
train_data = train_data.drop(cols_to_drop, axis=1)

#tussentijds resultaat
print(train_data.head())

#hier zetten wij alles om naar lower character. en halen wij alle gekke tekens eruit
train_data['text'] = train_data['text'].str.lower()
train_data['text'] = train_data['text'].apply(lambda elem: re.sub(r"(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", "", elem))
train_data['text'] = train_data['text'].apply(lambda elem: re.sub(r"\d+", "", elem))

#tussentijds resultaat
print(train_data.head())

#hier stellen wij de variabelen op om straks de tekst naar vectors om te zetten
count_vectorizer = feature_extraction.text.CountVectorizer()
#hier wordt onze train data omgezet naar vectors
train_vectors = count_vectorizer.fit_transform(train_data["text"])
#voorbeeld van de vectors
print(train_vectors)
#hier wordt onze test data omgezet naar vectors
test_vectors = count_vectorizer.transform(test_df["text"])

clf = MultinomialNB(alpha=1,fit_prior=True,class_prior=None)
scores = model_selection.cross_val_score(clf, train_vectors, train_data["target"], cv=3, scoring="f1")
print(scores)