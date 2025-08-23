# src/cleaning.py

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def fill_missing_median(df, cols=None):

    df_copy = df.copy()
    if cols is None:
        cols = df_copy.select_dtypes(include="number").columns
    for col in cols:
        median_val = df_copy[col].median()
        df_copy[col].fillna(median_val, inplace=True)
    return df_copy


def drop_missing(df, thresh=0.5):
   
    df_copy = df.copy()
    missing_fraction = df_copy.isnull().mean()
    drop_cols = missing_fraction[missing_fraction > thresh].index
    df_copy.drop(columns=drop_cols, inplace=True)
    df_copy.dropna(inplace=True)  # drop remaining rows with any NaN
    return df_copy


def normalize_data(df, cols=None):

    df_copy = df.copy()
    scaler = MinMaxScaler()

    if cols is None:
        cols = df_copy.select_dtypes(include="number").columns
    
    df_copy[cols] = scaler.fit_transform(df_copy[cols])
    return df_copy
