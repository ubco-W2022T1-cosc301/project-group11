import pandas as pd 
import numpy as np
import random
import seaborn as sns

def load_and_process(day, month, file):

    # Deletes all columns i dont want as well as finds the dates that i have chosen fron the past 18 years
    dataFrame = (
        pd.read_csv(file)
        .drop(columns=["YEAR", "HOUR", "MINUTE", "HUNDRED_BLOCK", "NEIGHBOURHOOD", "X", "Y"])
        .loc[lambda x: x["DAY"] == day]
        .loc[lambda x : x["MONTH" ]== month]
    )
    

    return dataFrame

def Make_To_Table(dataframe): 
    df = dataframe['TYPE'].value_counts(sort = True)
    dataframe = ( 
        pd.crosstab(index= 0, columns= dataframe["TYPE"])
        .assign(Total= df.sum())   
    )
    return dataframe


def Find_sig(dataFrame, std,mean):
    sigNumAbove = mean + (std*3)
    sigNumbelow = mean - (std*3)
    DataF = (
        pd.DataFrame(dataFrame)
        .assign(sigDiff = (dataFrame["Total"] > sigNumAbove ) )
        .drop(columns=['Theft from Vehicle', 'Theft of Bicycle', 'Theft of Vehicle',
       'Vehicle Collision or Pedestrian Struck (with Fatality)',
       'Vehicle Collision or Pedestrian Struck (with Injury)',
       'Break and Enter Commercial', 'Break and Enter Residential/Other',
       'Homicide', 'Mischief', 'Offence Against a Person', 'Other Theft'])
    )
    DataF = DataF[['Holiday', 'Total', 'sigDiff']]
    return DataF


def Rand_date(file):
    for x in range(100):
        a = random.randint(1,12)
        if a==1 or a ==3 or a==5 or a==7 or a ==8 or a== 10 or a==12:
            b = random.randint(1,31)
            place = load_and_process(b,a, file)
        elif a == 4 or a== 6 or a ==9 or a == 11:
            b = random.randint(1,30)
            place = load_and_process(b,a, file)
        else: 
            b = random.randint(1,28)
            place = load_and_process(b,a, file) 
        if x == 0: 
            df = place
            df = Make_To_Table(df)
        else:
            place = Make_To_Table(place)
            df = pd.merge(df,place, how = "outer")
    return df

def Find_mean(df):
    mean = df["Total"].mean()
    return mean

def Find_Std(df):
    std = df['Total'].std()
    return std

def Holidays(Holidays,day,month,file):
    df = load_and_process(day, month, file)
    df = Make_To_Table(df)
    df = df.assign(Holiday = Holidays)
    return df


def mrg(list):
    for x in range(len(list)):
        if x == 0:
            df = list[x]
        else: 
           df = pd.merge(df,list[x], how = "outer") 
    df = df[['Holiday', 'Theft from Vehicle', 'Theft of Bicycle', 'Theft of Vehicle',
       'Vehicle Collision or Pedestrian Struck (with Fatality)',
       'Vehicle Collision or Pedestrian Struck (with Injury)',
       'Break and Enter Commercial', 'Break and Enter Residential/Other',
       'Homicide', 'Mischief', 'Offence Against a Person', 'Other Theft', "Total"]]
    return df


def First_Mod():
    file = '../data/raw/crimedata_csv_all_years.csv'
    chisEve = Holidays('ChristmasEve', 25,12, file)
    chisDay = Holidays('ChristmasDay', 26,12, file)
    NewEve = Holidays('NewyearsEve', 31,12, file)
    NewDay =Holidays('NewyYearsDay', 1 ,1, file) 
    CanDay =Holidays('CanadaDay', 1 ,7, file)
    ValDay = Holidays('ValDay', 14 ,2, file) 
    Halloween =Holidays('Halloween',31, 10,file)
    list = [chisEve,chisDay,NewEve,NewDay,CanDay,ValDay,Halloween]
    Hcrim = mrg(list)
    return Hcrim

def Sec_Mod(Hcrim,df1):
    df1Mean =Find_mean(df1)
    df1Std = Find_Std(df1)

    SigDifference = Find_sig(Hcrim,df1Std,df1Mean)
    return(SigDifference)

def Third_Mod(Hcrim,df1):
    alldf = pd.merge(Hcrim, df1, how = 'outer')
    sns.boxplot(alldf, x= alldf['Total'])


