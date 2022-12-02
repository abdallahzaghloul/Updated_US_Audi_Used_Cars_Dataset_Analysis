
from PIL import Image
import streamlit as st
import pandas as pd
import numpy as np

data=pd.read_csv("C://Users//hp//Desktop//Data Science//Mid-Project//Data_Visulaization_Project_Files//audi.csv")

st.markdown(" <center>  <h1> Audi Car Data Set </h1> </font> </center> </h1> ",
            unsafe_allow_html=True)

def Data_Columns_Uniting (data):
    data.columns = data.columns.str.upper().str.strip()
    data.columns = data.columns.str.replace(' ', '_')

Data_Columns_Uniting(data)

data['KPL']=data['MPG'].apply(lambda x: x*0.425144)

data['KILOMETERSAGE']=data['MILEAGE'].apply(lambda x: x*19.10)

st.write(data)



def Count_Unique_Values (data):
    s=[]
    for i in data.columns:
        s.append(len(data[i].unique()))
    st.write(pd.DataFrame(s, data.columns))
    
def Null_Check (data):
    for item in data.columns:
        if data[item].isnull().sum()==1:
            st.write(item,"is not ready")
        elif data[item].isnull().sum()==0:
            st.write(item,"is ready")

option = st.selectbox("Audi Car Data Set Checking Methods ",('Counting Unique Values','Null Checking'))

if option == 'Counting Unique Values':
    Count_Unique_Values (data)
elif option == 'Null Checking':
    Null_Check (data)


# streamlit run "C:\\Users\\hp\\Desktop\\Data Science\\Mid-Project\\Data_Visulaization_Project_Files\\Pages\\Audi_Car_Dataset.py"



