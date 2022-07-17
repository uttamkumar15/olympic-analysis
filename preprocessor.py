import pandas as pd

def preprocess(df,df_region):
    #filtering for Summer Olympics
    df = df[df["Season"]=='Summer']
    #merge df with df_region
    df = df.merge(df_region,on='NOC',how='left')
    #removing Duplicates Values
    df.drop_duplicates(inplace=True)
    #COncating the Medal Column
    df = pd.concat([df,pd.get_dummies(df['Medal'])],axis=1)
    return df