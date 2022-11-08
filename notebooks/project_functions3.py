import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns


def load(load_and_process):
    
    # Loads the data and removes missing data
    df = (
        
        pd.read_csv(load_and_process)
        .rename(columns = {"HUNDRED_BLOCK":"HUNDRED BLOCK"})
        .rename(str.title, axis = 'columns')
        .dropna()

    )
    
 # Set categorical data
    df['Type'] = df['Type'].astype('category')
    df['Neighbourhood'] = df['Neighbourhood'].astype('category')
    df['X'] = df['X'].astype('float64')
    df['Y'] = df['Y'].astype('float64')
    
    return df

def process(df):
    
     # Drop columns, create new variables, and do processing
     df_cleaned = (
        df
        .drop([ 'Year','Month','Day','Hour','Minute'], axis = 1)
        .sort_values(by = ['Hundred Block'])
    )
    
     return df_cleaned

def write(df, load_and_process):
    
    # Write data into CSV file
    df.to_csv(load_and_process)
    
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
    
def countplot(df, var, t, x):
    
    # Create countplot without hue
    sns.countplot(y = df[var]).set(title = t, xlabel = x)
    
def preview(df):
    
    # Generate preview of entries with null values
    if df.isnull().any(axis = None):
        print("\nPreview of data with null values:\nxxxxxxxxxxxxx")
        print(df[df.isnull().any(axis = 1)].head(3))
        missingno.matrix(df)
        plt.show()

def duplicates(df):
    
    # Generate count statistics of duplicate entries
    if len(df[df.duplicated()]) > 0:
        print("No. of duplicated entries: ", len(df[df.duplicated()]))
        print (df[df.duplicated(keep = False)].sort_values(by = list(df.columns)).head())
    else:
        print("No duplicated entries found")