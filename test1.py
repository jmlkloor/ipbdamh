import nltk
from nltk.tokenize import word_tokenize
import pandas as pd

train_df = pd.read_csv(r"C:\Users\Kevin\Desktop\train.csv",low_memory=False)

pd.set_option('display.max_columns', None)

train_df2 = pd.DataFrame.drop(train_df,columns=["keyword","location"])

print(train_df2)

lenpd = len(train_df2)
print(lenpd)

i = 0

new = pd.DataFrame()
while i < lenpd:

    tekst = train_df2["text"][i]

    print(tekst)

    new_tokens = nltk.pos_tag(word_tokenize(tekst))
    print([s for s in new_tokens if s[1] == 'NN'])

    train_df3 = pd.DataFrame.append(new,other=[s for s in new_tokens if s[1] == 'NN' or s[1] == 'NNS'])

    i = i + 1


#column=["text1", "text2"], value=[s for s in new_tokens if s[1] == 'NN'],loc=id(1)