"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.5
"""
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

def drop_features (df: pd.DataFrame):
    df_dropped = df.drop(columns= ['Age', 'Cabin', 'Embarked'])
    return df_dropped

def encode (df: pd.DataFrame):
    ordinal_encoder = OrdinalEncoder()
    features = ['Name','Sex', 'Ticket']
    df[features]= ordinal_encoder.fit_transform(df[features]) 
    df_encoded = df
    return df_encoded   

def scale (df: pd.DataFrame):
    scaler = MinMaxScaler()
    dfe_NParray = scaler.fit_transform(df)
    df_scaled = pd.DataFrame(dfe_NParray, columns=df.columns)
    return df_scaled    

    
