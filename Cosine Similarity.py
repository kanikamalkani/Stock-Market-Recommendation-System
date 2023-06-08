# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 00:39:12 2023

@author: kanik
"""

# https://medium.com/grabngoinfo/recommendation-system-user-based-collaborative-filtering-a2e76e3e15c4 

 

#importing the libraries 

import pandas as pd 

import numpy as np 

 

#importing the dataset 

df=pd.read_csv("dataset11.csv") 

 

#data preprocessing 

#CHECKING NULL VALUES 

df["P/E"].isnull().sum() 

 

 

#summary 

df.info() 

df.columns.values 

print("% of NULL : ",df.isnull().sum()/len(df)*100) 

 

for i in df: 

    if df[i].isnull().sum()==0: 

        print("No null values in", i) 

    else: 

        #imputed using mean 

        mean_weight = df[i].mean() 

        df[i].fillna(mean_weight,inplace=True) 

        print("Imputed Null Values in", i) 

 

#checking for null values after imputing 

 

print("% of NULL : ",df.isnull().sum()/len(df)*100) 

 

 

#COSINE SIMILARITY 

 

from sklearn.metrics.pairwise import cosine_similarity 

 

print(cosine_similarity(arr1[1],arr1[2])) 

 

#dropping identfiers 

df1=df.drop(['Name',"S.No."], axis=1) 

 

import seaborn as sns 

 

hm1=pd.read_csv("heatmap.csv") 

 

sns.heatmap(hm1) 

 

# Display the Pharma Sector Heatmap 

 

#the cosine similarity matrix 

stock_similarity_cosine = cosine_similarity(df1.fillna(0)) 

 

 

name = input('Which stock would you like to pick?\n') 

df.set_index("Name", inplace = True) 

hi=df.loc[name] 

stock_n=(hi['S.No.']) 

print(stock_n) 

# Number of similar users 

n = input("How many number of similar stocks do you want to find?\n") 

stock_n=int(stock_name) 

print(stock_n) 

list1=stock_similarity_cosine[stock_name2] 

list1=list(list1) 

#list2=list1.sort(reverse=True) 

lst=list(range(0,4187)) 

 

ind_stock = pd.DataFrame(list(zip(lst, list1)),columns =['index', 'val']) 

list1 

df5=ind_stock.sort_values("val",ascending=False) 

df5=df5.drop(index=0,axis=0) 

df3 = pd.DataFrame(stock_similarity_cosine) 

# User similarity threshold 

stock_similarity_threshold = 0.8 

n_similar=list(df5["index"].head(n)) 

#float(n_similar) 

#nn=df.head(11) 

print(n_similar) 

for i in n_similar: 

    print(df._get_value(i, 'Name')) 

 