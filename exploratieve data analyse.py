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

print(train_df['Uppercase'].sum())
print(train_df['Lowercase'].sum())

#lengte van de teksten
train_df['Text_Lengt'] = train_df['text'].apply(len)

print(train_df.head(5))
#max van lengtetekst
print(train_df['Text_Lengt'].max())
#min van lengtetekst
print(train_df['Text_Lengt'].min())

#splitten van data in een dataframe voor 0 en voor 1
Dataframe0 = train_df[train_df.target == 0]
Dataframe1 = train_df[train_df.target == 1]

print(Dataframe0.head(5))
print(Dataframe1.head(5))

#printen van gemiddelde text lengte van 0 dataframe en van 1 dataframe
print("0:",Dataframe0['Text_Lengt'].mean())
print("1:",Dataframe1['Text_Lengt'].mean())

print("gem.upper.0:",Dataframe0['Uppercase'].sum())
print("gem.lower.0:",Dataframe0['Lowercase'].sum())

print("gem.upper.1:",Dataframe1['Uppercase'].sum())
print("gem.lower.1:",Dataframe1['Lowercase'].sum())
