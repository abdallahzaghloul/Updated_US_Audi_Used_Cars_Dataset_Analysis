import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

data=pd.read_csv("audi.csv")


def Data_Columns_Uniting (data):
    data.columns = data.columns.str.upper().str.strip()
    data.columns = data.columns.str.replace(' ', '_')

Data_Columns_Uniting(data)



fig_1 = px.histogram(data, x="MODEL", color="FUELTYPE", facet_col="TRANSMISSION",marginal='violin')
fig_2 = px.scatter(data, x="MODEL", y="PRICE", color="FUELTYPE", facet_col="TRANSMISSION")
fig_3 = px.scatter(data,x='YEAR', y='ENGINESIZE', size='PRICE', marginal_x='violin', marginal_y='box', color='PRICE')
fig_4 = px.pie(data,names ='MODEL',values='YEAR')
fig_5 = px.pie(data,names ='TRANSMISSION',values='YEAR')
fig_6 = px.pie(data,names ='FUELTYPE',values='YEAR')

st.markdown(" <right>  <h1>  Audi Car Data Set Graphical Representation </h1> </font> </right> </h1> ",
            unsafe_allow_html=True)

T1,T2,T3,T4= st.tabs(["Models Availability","Model Vs. Prices","Years Vs. Engine_Size ","Models Share %"])

T1.subheader("Model Availability")
T1.plotly_chart(fig_1, use_container_width=True)


T2.subheader("Model Vs. Prices")
T2.plotly_chart(fig_2, use_container_width=True)


T3.subheader("Years Vs. Engine_Size ")
T3.plotly_chart(fig_3, use_container_width=True)

T4.subheader("Models Share %")
T4.plotly_chart(fig_4, use_container_width=True)
T4.write('This is a simple pie chart showing that the most populatr car is the (A3) by (18.1 %)regardless car modes, prices and mileages')
T4.plotly_chart(fig_5, use_container_width=True)
T4.write('This one is showing the less relative differences between the sharing of the car modes, however, the manual car mode one is cummulatively the highest')
T4.plotly_chart(fig_6, use_container_width=True)
T4.write('This one is showing that approximately the used car are shared between the Diesel and Petrol cars while the hybrid one could be neglected')

T1.write('This chart is showing that the most common used cars are the manual mode (diesel) cars ')
T2.write('This chart is showing that the manual mode cars are relatively lower in their prices. That returns to the old manufacturing ' )
T3.write('This chart is showing that the older the car the lower the engine size but also the price is effected. Generally, the new cars are with high engine size even for the same model but higher in price')

# streamlit run "C:\\Users\\hp\\Desktop\\Data Science\\Mid-Project\\Data_Visulaization_Project_Files\\Pages\\Audi_Car_Dataset _Chart.py"
# pipreqs --encoding=utf8



