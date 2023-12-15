import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(
    page_title="Exploratory Data Analysis",
    page_icon="📊")

st.title('📊 Exploratory Data Analysis')

st.info('This demo shows the use of Pandas for loading data as DataFrames and Altair for chart creation.')

st.subheader('Which Movie Genre performs best at the box office?')

# Load data
df = pd.read_csv('data/movies_genres_summary.csv')

# Placeholder
placeholder1 = st.empty()
placeholder2 = st.empty()

# Input widgets
## Genres selection
genres_list = df.genre.unique()
genres_selection = st.multiselect('Select genres', genres_list, ['Action', 'Adventure', 'Biography', 'Comedy', 'Drama', 'Horror'])
## Year selection
year_list = df.year.unique()
year_selection = st.slider('Select year duration', 1986, 2006, (2001, 2006))

df_selection = df[ df.genre.isin(genres_selection) ]

st.write(np.arange(year_selection[0], year_selection[1]+1))

# Display DataFrame
with placeholder1:
    df_editor = st.data_editor(df_selection, height=212, use_container_width=True, hide_index=True)

# Display chart
with placeholder2:
    st.line_chart(df_selection, x='year', y='gross', color='genre')
