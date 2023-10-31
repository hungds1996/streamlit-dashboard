import streamlit as st
from processing import *
import pandas as pd
from pathlib import Path


data = pd.read_csv(Path(__file__).parents[0]/'data.csv')
df = pd.DataFrame()

# Basic layout config
st.set_page_config(page_title='Dashboard', layout='wide')
st.markdown("<h1 tyle='text-align: center; color: black;'>Dashboard</h1>", unsafe_allow_html=True)

buffer, col2, col3 = st.columns([1, 5, 15])

# filter data feature
with col2:
    key = st.selectbox("Key", list(data.columns))

# filter the df based on column name and a value
with col3:
    search_term = st.text_input("Search")
    if key != '' and search_term != '':
        df = search(data, key, search_term)
    else:
        df = data

# display the df        
buffer, col2 = st.columns([1, 20])
with col2:
    if not df.empty:
        st.dataframe(df)
    else:
        st.write("Did not find any matching result")

st.markdown("***")

buffer, col2, col3, col4 = st.columns([1, 7, 7, 7])

with col2:
    st.markdown("<h5 style='text-align: center; color: black;'>Gender Distribution</h1>", unsafe_allow_html=True)
    st.pyplot(pie_chart(get_distribution(df, 'Gender')))
    
with col3:
    st.markdown("<h5 style='text-align: center; color: black;'>Age Distribution</h1>", unsafe_allow_html=True)
    st.bar_chart(get_distribution(df, 'Age'))
    
with col4:
    st.markdown("<h5 style='text-align: center; color: black;'>Country Distribution</h1>", unsafe_allow_html=True)
    st.pyplot(pie_chart(get_distribution(df, 'Country')))
    
st.markdown('***')

buffer, col2, col3 = st.columns([1, 10, 10])

with col2:
    st.markdown("<h5 style='text-align: center; color: black;'>Average salary per profession</h1>", unsafe_allow_html=True)
    st.bar_chart(relate_data(df, 'Profession', 'Salary'))
    
with col3:
    st.markdown("<h5 style='text-align: center; color: black;'>Average salary per age group</h1>", unsafe_allow_html=True)
    st.bar_chart(relate_data(df, 'Age', 'Salary'))
    
st.markdown('***')
buffer, col2 = st.columns([1, 20])

with col2:
    st.markdown("<h5 style='text-align: center; color: black;'>Accumulated signups over time</h1>", unsafe_allow_html=True)
    st.line_chart(accumulated_signups(get_signups(df, dt.datetime(2020, 1, 1), dt.datetime(2022, 12, 31))))