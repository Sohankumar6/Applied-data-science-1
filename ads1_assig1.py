# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 15:09:20 2023

@author: sohan 
"""
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("mcdonalds_dataset.csv")
# Exploratory data analysis
data.head()
print(data.shape)
print(data.columns)
print(data.dtypes)
data.info()
data.isnull().sum()
data=data.dropna()
data.head(20)
data= data.drop(['url_for_product','product_availability','have_sizes'], axis='columns')
data['product_calories'] = data['product_calories'].str.replace('kcal: ', '')
data['product_calories'] = data['product_calories'].str.replace('kcal: ', '').astype(int)
data_sub= data.sort_values(by=['product_calories'])
data_sub1= data.sort_values(by=['product_price'])

def line():
    '''This function creates a line plot comparing cahnge in price according to calories '''
    plt.plot(data_sub['product_calories'][:50],data_sub1['product_price'][:50],color='cyan',
             label='Calorie, in kcal')
    plt.plot(data['Carbs'][:50], data_sub1['product_price'][:50], color='orange',label='Carbs, in g')
    plt.plot(data['Protein'][:50], data_sub1['product_price'][:50], color='yellow',label='Protien, in g')
    plt.xlabel("Calories, Protein and Carbs")
    plt.ylabel("Product price")
    plt.title("Changes in price according to changes in calories count, protein, carbs")
    plt.legend()
    plt.xticks(rotation=90)
    plt.show()
def barplot():
    '''This function plots a barchart for calorie count in each product'''
    plt.figure(figsize=(8,8))
    plt.bar(data['product_name'][:50],data_sub['product_calories'][:50],color='Violet')
    plt.xlabel("Product_Name")
    plt.ylabel("Calorie_Count in kcal")
    plt.title("Calorie_per_product")
    plt.xticks(rotation=90)
    plt.show()
def histo():
    '''This function plots a histogram'''
    plt.figure(figsize=(10,10))
    plt.hist(data_sub['Sugars'],bins=50,color='red')
    plt.xlabel("Sugar Content in g")
    plt.title("Sugar Content Distribution")
    plt.xticks(rotation=90)
    plt.show()
line()
barplot()
histo()
