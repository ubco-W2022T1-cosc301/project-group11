# Group 11 Final Report

## Introduction

The dataset selected for this project is created by Sumaia P. and is posted on Kaggle. The data collection lists Vancouver's historical crime data from 2003 to 2021. The table shows the type of crime, the year, month, date, hour, and minute that they occurred, the location (hundred block) and neighborhood of the crime scene, and the x and y coordinate values projected in UTM zone 10. This collection has been released to the public by the Vancouver Police Department (VPD) with the intention of enhancing community awareness of policing activities in the city. The data provided is based on the information contained in the VPD Records Management System. Unfortunately, there is no information on how the data was collected. Still, it can be speculated that the values are based on historical records that have been digitized, as the historical crime data of past years are likely archived into a dataset such as this.

We are very interested to find out the historical crime trends in Vancouver, as it is a city we visit often, and some of us are even planning to move there in the future. By gaining more awareness, we will be able to be more prepared to avoid encountering these crimes. The crime data will also likely be a valuable reference for the police department of Vancouver to predict crimes that may occur in the future and prepare means to handle them better.

The questions that we would be exploring are:

1. Does the total crime committed during the holiday season increase or decrease? (Luca)
2. At what times and years do the crimes occur the most? (Ken)
3. Which areas are the most targeted? (eg. residential areas, business districts, parking lots, etc.) (Adnan)

&nbsp;

## Explatory Data Analysis

### Question 1



### Question 2 (At what times and years do the crimes occur the most?)

#### **1. Understanding the Variables**

![head](./images/Q2/head.png)

From the first 5 rows out of the 793916 rows of the dataset, it can be seen that there are 10 columns which are the `Type` of crime, the `Year`, `Month`, `Day`, `Hour`, `Minute`, `Hundred Block`, `Neighbourhood`, and the `X` and `Y` coordinates projected in UTM Zone 10. From what can be seen, the table only shows Theft from Vehicle in the same hundred block, neighbourhood, and x and y coordinates, but at different times. It is not likely for the entire dataset to contain only this type of crime at this location, and the output below has indicated so.

![nunique](./images/Q2/nunique.png)

It can be seen that there are indeed other types of crimes other than `Theft from Vehicle` as there are more than 1 type. There are 19 years spanned by the data, however, it is not known what the starting and ending year is at the moment. There also seems to be a wide range of areas covered from looking at the number of hundred blocks and neighbourhood present in the data.

![numerical](./images/Q2/numerical.png)

The numerical variable information shows that the dataset spans the years 2003 to 2021 with crimes occurring at a mean hour during 12 noon.

![discrete](./images/Q2/discrete.png)

The discrete variable information shows that there are 11 types of different values for the type of crimes. There are indeed 11 unique strings shown in the block above. Only a handful of the hundred block is printed due to the overwhelming number of 22939 unique values. All the 24 neighbourhood values are displayed alongside as well.

#### **2. Cleaning the Dataset**

The objective of this section is to clean the dataset in order to avoid any misleading data and to remove unused blocks. The procedure would be to remove redundant variables, make a better variable selection, remove outliers, and removing null value rows.

Although having more information may seem better at first glance, there are times when too much information becomes too distracting. The research question that would be explored further in this analysis is "At what times and years do the crimes occur the most?". In this case, as there would be a heavy emphasis on time and date, and less on location, the variables that contain information about the crime locations become redundant. These include the `Hundred Block`, `Neighbourhood`, `X`, and `Y` columns specifically. All these columns will be removed.

The following step is to remove any columns that have enough null values that may affect the analysis results later. As there are no null values in the data, this dataset cleaning step can be skipped.

Next would be to check for any outlier values. From the numerical information table, it shows that the range of values for `Month`, `Day`, and `Hour` are 1-12, 1-31, and 0-23 respectively. These ranges are as expected for their respective variables, thus there are no outliers to be deleted. Another important factor to consider is the range of datetime covered by each year. As it is required for all the years to cover cases reported from January to December for an equal data distribution, the start and end date for this dataset have to be validated. In order to do this, a new column will be added called 'datetime', and from this column, the maximum and minimum value can be obtained. The output shows that the dataset starts from the beginning of 2003 but stops midway through 2021. For a more equally distributed data, all values from 2021 will be removed.

The last step consists of removing rows with null values, however, it is previously known that there are no existing null values in the dataset, hence no further data altering would be required.

The final cleaned dataset is as follows:

![cleaned](./images/Q2/df_cleaned.png)

#### **3. Variable Analysis**

![corr](./images/Q2/corr.png)

A correlation matrix is useful for picking out any relationship between each variables. The numbers in each box of the graph show the correlation coefficients, which are the numerical representation of how close the two variables are related to each other. The numbers range from 0 up to 1, where 0 signifies no relationship and 1 represents that they are fully dependent on each other. These values can also become negative if there is a negative correlation between them, meaning that an increase of a variable leads to a decrease of the other. The results show that there are barely any correlation between each variable, with a mere maximum coefficient value of 0.11. This means that each column of the dataset do not rely on each other and would be more effective to analyze each variable separately.

![casesbyyear](./images/Q2/casesbyyear.png)

Each variable will be plotted using a countplot for the analysis. From the result above, there seem to be a parabolic relationship between the crime rates throughout the years with a few exceptions. 2003 started with the largest crime rate frequency, slowly decreasing until the turning point of 2011, where it began to increase up until 2019. The crime rate in 2020 dropped by a fair amount likely due to the pandemic.

![casesbymonth](./images/Q2/casesbymonth.png)

The countplot of the relationship between the crime rates and the months shows a fairly linear graph. August had the most frequency while February had the least, however, by only a margin of about 1000 crimes. Not much can be deduced from this other than that the crime rates are equally split between the months in each year, thus the occurrence of crime rates are not likely to depend on the month.

![casesbyday](./images/Q2/casesbyday.png)

From the result of this countplot, it is shown that the most occurrence day of crime is on the 1st, followed by the 15th. At the beginning of each month and exactly midway through the months are when crimes happen the most, with a steady rate in between this duration, and a slight decrease after the 15th. The 31st has significantly less crime rates likely due to the fact that this day exists only in half of the months in each year.

![casesbyhour](./images/Q2/casesbyhour.png)

Criminal cases occur the most frequent at midnight and leads other hours by a large amount. At 6 p.m. is the next frequent hour. There is a trend of criminal cases happening more often during late evening and especially during midnight, however, drops significantly during the early morning.

![casesbymin](./images/Q2/casesbymin.png)

The occurrence of criminal cases happen the most frequently on the 0th minute followed by the 30th by a far margin. The frequency for the other minutes are very little in comparison. It is likely that most cases have the minutes rounded to the nearest hour or half-hour.

![casesbytypeandyear](./images/Q2/casesbytypeandyear.png)

From the graph above, it can be observed that "Theft from Vehicle" and "Other Theft" are the major contributors to the number of crime rates throughout the years. "Break and Enter Residential/Other" and "Theft of Vehicle" criminal records have shown a decreasing trend as the years passed. On the other hand, "Break and Enter Commercial", "Mischief", "Other Theft", and "Theft from Vehicle" showed a parabolic curve where the crime rate starts high, dips down, and rises up again. "Theft of Bicycle" has been gradually increasing since 2003, and "Offence Against a Person" and "Vehicle Collision or Pedestrian Struck (with Injury)" remained consistent throughout the years. From these observations, it is generalized that while home security has improved over the years, vehicle security has not. The crime rates would drastically reduce if vehicle manufacturers find a way to further enhance their security systems or if the general public avoid leaving their vehicle unattended for too long.

![casesbytypeandhour](./images/Q2/casesbytypeandhour.png)

There is an overwhelming amount of crime for an "Offence Against a Person" which seems to occur only during midnight. The general public should avoid going outdoors alone at this time to reduce the risks of being a victim for this type of crime. The general trend for each type of crime is that the most occurrence time is during midnight, with a few exceptions. "Theft from Vehicle" and "Other Theft" also have a high occurrence during the afternoon to late evening. It may be an option for the police department to increase patrolling during these hours to reduce the risks of such criminal activities to occur.

### Question 3



## Conclusion

It is observed that the most occurred crime rate year is 2003 and despite showing an improvement on the occurrence the following few years, has begun to rise again from 2011. There is however, a significant drop during 2020 likely due to the upsurge of the epidemic. The most occurred crime rate month is August, but due to the marginal differences throughout the months, it is likely that the month does not play a significant role in the crime rate. Criminal activities are most likely to occur during midnight as from the observations, which are largely classified as "Offense Against a Person", followed by "Theft of Vehicle" and "Other Theft".

From these observations, we can predict that the crime rate will begin to increase again in the following years do to the pandemic settling down, with a fairly constant rate throughout the months. "Theft of Vehicle" and "Other Theft" are still likely to be the main contributors to the amount of crime, mostly occurring during the midnight and late evening. During midnight, "Offense Against a Person" is still likely to be a risk especially.

It is best for the general public to be wary when leaving the house during midnight, especially if alone, as well as leaving their vehicle unattended for a long period of time in an environment with low security. Valuables should be taken out of the car whenever unused, and the windows and doors should be properly locked. The police department should develop a plan for reducing the crime rates especially for thefts as they are the largest contributor, whether that be to increase patrolling or to improve security systems or by other means.
