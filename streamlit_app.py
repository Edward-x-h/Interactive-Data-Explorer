import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from data_processing import process_data


# Page title
st.set_page_config(page_title='Interactive Data Explorer', page_icon='📊')
st.title('📊 Interactive Data Explorer')

with st.expander('About this app'):
  st.markdown('**What can this app do?**')
  st.info('This app shows the use of Pandas for data wrangling, Altair for chart creation and editable dataframe for data interaction.')
  st.markdown('**How to use the app?**')
  st.warning('To engage with the app, 1. Select genres of your interest in the drop-down selection box and then 2. Select the year duration from the slider widget. As a result, this should generate an updated editable DataFrame and line plot.')
  
st.subheader('Which Movie Genre performs ($) best at the office?')

# Load data
cleaned_data = process_data('test1.csv')
cleaned_data.to_csv('cleaned_data.csv', index=False)
df = pd.read_csv('cleaned_data.csv')

