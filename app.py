# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 22:43:25 2021

@author: Irfan Sheikh
"""

import streamlit as st
import pandas as pd
import numpy as np
from datetime import date
import matplotlib.pyplot as plt
import seaborn as sns
import os
os.chdir("D://Data Science//Project//P44 Sales Forecasting Excelr")

plt.style.use('fivethirtyeight')
sns.set()
pd.set_option('display.max_rows',5000)

st.title("Retail Customer Predictor")

def get_data(suppress_st_warning=True):
    path=path=r"Ecommerce1.csv"
    return pd.read_csv(path)

data=get_data()

page_bg_img = '''
<style>
body {
background-image: url("https://www.google.com/imgres?imgurl=https%3A%2F%2Fi.ytimg.com%2Fvi%2FznijFGYNjmA%2Fmaxresdefault.jpg&imgrefurl=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DznijFGYNjmA&tbnid=Eb37v8MNP1oXVM&vet=12ahUKEwiH-Y-avdjvAhXMEnIKHWfAAJ8QMygIegUIARCnAQ..i&docid=LGgQ9GterEH6gM&w=1280&h=720&q=excelr&ved=2ahUKEwiH-Y-avdjvAhXMEnIKHWfAAJ8QMygIegUIARCnAQ");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

data.drop_duplicates(keep=False,inplace=True)
data=data.drop(["RecencyCluster","FrequencyCluster","RevenueCluster","OverallScore","DayDiff","DayDiff2","DayDiff3","DayDiffMean","DayDiffStd","Segment_High-Value","Segment_Low-Value","Segment_Mid-Value"],axis=1)

data["NextPurchaseDate"]=pd.to_datetime(data["NextPurchaseDate"])




start_date=st.sidebar.date_input("Start date",date(2012,1,1))
end_date=st.sidebar.date_input("End date",date(2012,1,31))
start_date=pd.to_datetime(start_date)
end_date=pd.to_datetime(end_date)

if start_date>=end_date:
    st.error("Please enter a valid date")
#sidebar New_revenue3

min_revenue=int(data["New_Revenue"].min())
max_revenue=int(data["New_Revenue"].max())

selected_revenue_range=st.sidebar.slider("Select the Expected Revenue Range",0,max_revenue,min_revenue)

data_filtered=data[(data["NextPurchaseDate"]>=start_date) & (data["NextPurchaseDate"]<=end_date)]

st.dataframe(data_filtered)
