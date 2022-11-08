import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns

def load(path_to_file):
    
    # Load data and deal with missing data
    df = (
        pd.read_csv(path_to_file)
        .rename(columns = {"HUNDRED_BLOCK": "HUNDRED BLOCK"})
        .rename(str.title, axis = 'columns')
        .dropna()
    )
    
    # Set categorical data
    df['Type'] = df['Type'].astype('category')
    df['Hundred Block'] = df['Hundred Block'].astype('category')
    df['Neighbourhood'] = df['Neighbourhood'].astype('category')
    
    return df

def process(df):
    
     # Drop columns, create new variables, and do processing
    df_cleaned = df.drop(['Hundred Block', 'Neighbourhood', 'X', 'Y'], axis = 1)
    df_cleaned = (
        df_cleaned
        .drop(df_cleaned[df_cleaned.Year == 2021].index)
        .assign(Datetime = pd.to_datetime(df_cleaned.drop(['Type'], axis = 1)))
        .sort_values(by = ['Datetime'])
    )
    display(df_cleaned)
    
    return df_cleaned

def write(df, path_to_file):
    
    # Write data into CSV file
    df.to_csv(path_to_file)
    
def head(df):
    
    # Display head of data
    display(df.head())
    
def shape(df):
    
    # Display shape of data
    print(df.shape)
    print(f"The number of rows is {df.shape[0]} and the number of columns is {df.shape[1]}")
    
def col(df):
    
    # Display column names
    print(df.columns)
    
def nunique(df):
    
    # Display number of unique values for each column
    print(df.nunique(axis = 0))
    
def numerical(df):
    
    # Display summary of numerical variables
    display(df.describe().apply(lambda s: s.apply(lambda x: format(x, 'f'))))
    
def discrete(df):
    
    # Display unique values for discrete variables
    print(df.Type.unique())
    print(df['Hundred Block'].unique())
    print(df.Neighbourhood.unique())
    
def corr(df):
    
    # Create correlation matrix
    corr_matrix = df.corr()
    sns.heatmap(corr_matrix, xticklabels = corr_matrix.columns, yticklabels = corr_matrix.columns, annot = True, cmap = sns.diverging_palette(220, 20, as_cmap = True))
    
def countplot(df, var, t, x):
    
    # Create countplot without hue
    sns.countplot(y = df[var]).set(title = t, xlabel = x)
    
def countplothue(df, var, h, t, x):
    
    # Create countplot with hue
    sns.countplot(data = df, y = var, hue = h, palette = 'muted').set(title = t, xlabel = x)
    sns.set(rc = {'figure.figsize': (12, 30)})