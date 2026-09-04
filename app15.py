import streamlit as st
import numpy as np
import pandas as pd
import pickle

st.title("Car Price Prediction App")
import streamlit as st
st.markdown("""
<style>
.stButton > button {
    background-color: #7C3AED;
    color: white;
    border-radius: 8px;
    border: none;
    font-weight: 600;
}

.stButton > button:hover {
    background-color: #6D28D9;
    color: white;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
.stApp {
    background-color: #EAF4FF;
}
</style>
""", unsafe_allow_html=True)


import streamlit as st

st.markdown("""
<style>

/* Main background */
.stApp {
    background-color: #F3E8FF;
}

/* Sidebar background */
[data-testid="stSidebar"] {
    background-color: #E9D5FF;
}

</style>
""", unsafe_allow_html=True)
pipe = pickle.load(open("final_file.pkl", "rb+"))
df = pd.read_csv("Cleaned_data.csv")
companies = sorted(df["company"].unique())
years = range(2000, 2027)

company = st.sidebar.selectbox("Select company", companies)

names = sorted(df[df['company'] == company]["name"].unique())

name = st.sidebar.selectbox("Select name", names)
year = st.sidebar.selectbox("Select year", years)
km_driven = st.sidebar.number_input("Enter km driven", value=50000, min_value=1000, max_value=200000, step=1000)
fuel = st.sidebar.selectbox("Select fuel type", ["Petrol", "Diesel"])

if st.sidebar.button("Predict Price"):
    st.write("You have selected:")
    st.write(f"Company: {company}") 
    st.write(f"Name: {name}")
    st.write(f"Year: {year}")
    st.write(f"Kilometers Driven: {km_driven}")
    st.write(f"Fuel Type: {fuel}")
    #check for user input
    myinput = [[company, name, year, km_driven, fuel]]
    columns = ['company', 'name', 'year', 'kms_driven', 'fuel_type']
    myinput = pd.DataFrame(data = myinput, columns = columns)
    result = pipe.predict(myinput)

    if result[0,0] < 0:
        st.write("Sorry, the predicted price is negative. Please check your input values.")
    else:
        st.write("Predicted price is:", str(round(result[0,0])))
