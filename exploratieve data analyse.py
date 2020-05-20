import pandas as pd

train_df = pd.read_csv(r"C:\Users\Kevin\Desktop\train.csv",low_memory=False)

pd.set_option('display.max_columns', None)

print(train_df.head(5))

#count op null waardes
print(train_df.isnull().sum())

#count aantal 0 en 1
print(train_df.groupby('target').count())

#count op letters met een uppercase
train_df['Uppercase'] = train_df['text'].str.count(r'[A-Z]')
#count op letters met een lowercase
train_df['Lowercase'] = train_df['text'].str.count(r'[a-z]')

print(train_df.head(5))

#lengte van de teksten
train_df['Text_Lengt'] = train_df['text'].apply(len)

print(train_df.head(5))
#max van lengtetekst
print(train_df['Text_Lengt'].max())
#min van lengtetekst
print(train_df['Text_Lengt'].min())

