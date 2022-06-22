#Import packages
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#Import datasets
df_Cab= pd.read_csv("Cab_Data.csv")
df_City= pd.read_csv("City.csv")
df_Customer_ID= pd.read_csv("Customer_ID.csv")
df_Transaction_ID= pd.read_csv("Transaction_ID.csv")

#First Exploratory of data
print(df_Cab.head())
print(df_City.head())
print(df_Customer_ID.head())
print(df_Transaction_ID.head())

print(df_Cab.tail())
print(df_City.tail())
print(df_Customer_ID.tail())
print(df_Transaction_ID.tail())

#Describe data(Understand the field names and data types)
print(df_Cab.describe())
print(df_City.describe())
print(df_Customer_ID.describe())
print(df_Transaction_ID.describe())

print(df_Cab.shape)
print(df_City.shape)
print(df_Customer_ID.shape)
print(df_Transaction_ID.shape)

print(df_Cab.nunique())
print(df_City.nunique())
print(df_Customer_ID.nunique())
print(df_Transaction_ID.nunique())

#Clean the data(Field/feature transformations)
print(df_Cab.isnull().sum())
print(df_City.isnull().sum())
print(df_Customer_ID.isnull().sum())
print(df_Transaction_ID.isnull().sum())

#Create master data named data
#Join dataframes 'Cab_Data', 'Customer_ID', 'Transaction_ID' 
data1= pd.merge(df_Cab, df_Transaction_ID)
print(data1)
data2= pd.merge(data1, df_Customer_ID)
print(data2)

#Append 'data2' and 'City' dataframes
#data= data2.append(df_City)
#print(type(data))

#Remove annoying variables 'Customer ID', 'Transaction ID'
data=data2.drop(['Customer ID', 'Transaction ID', 'City', 'Payment_Mode'], axis=1)

print(data.shape)
#Dummy coding
data= pd.get_dummies(data)

print(data.head())
print(data.shape)


#Relationship Analysis
#between all variable in data
correlation = data.corr()
heatmap = sns.heatmap(correlation, xticklabels=correlation.columns, yticklabels= correlation.columns, annot=True)
plt.show()

#2 by 2 Between variables in data
sns.pairplot(data)
plt.show()

#Between 'Company' and 'Users',and 'Price'
sns.relplot(x='Price Charged', y='Cost of Trip', hue= 'Company_Yellow Cab', data= data)

#Between 'Company' and 'Users',and 'Cost of Trip'
#sns.relplot(x='Cost of Trip', y='', hue= 'Company_Yellow Cab', data= df_Cab)
plt.show()

#Display Histograms
#For 'Company'
#sns.distplot(data['Company_Yellow Cab'], bins=5)
plt.show()

#For 'Users'
#sns.distplot(data['Company_Pink Cab'], bins=5)

#For 'Cost of Trip'
sns.distplot(data['Cost of Trip'], bins= 20)
plt.show()

#Identify and remove duplicates
data.drop_duplicates(subset=None, keep='first', inplace=False)
plt.show()
#Perform other analysis like NA value and outlier detection
#Box plot for all relationship in the data dataset
#sns.catplot(x='Company_Yellow Cab', kind='box', data=data)
#sns.catplot(x='Company_Pink Cab', kind='box', data=data)
sns.catplot(x='Cost of Trip', kind='box', data=data)
sns.catplot(x='Price Charged', kind='box', data=data)

#Show all plot
plt.show()









