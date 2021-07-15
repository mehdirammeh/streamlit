import streamlit as st

import pandas as pd


st.title('Hello Wilders, welcome to my application!')

#Afficher un élément:
st.write("I enjoy to discover stremalit possibilities")


link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/weather2019.csv"

df_weather = pd.read_csv(link)

#Afficher le dataframe:
st.write(df_weather) #ou directement avec la "magic command" df_weather directement

#Afficher un graphique:
st.line_chart(df_weather['MAX_TEMPERATURE_C'])

#ou encore avec les librairies qu'on connait déjà:
import seaborn as sns

viz_correlation = sns.heatmap(df_weather.corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)
st.pyplot(viz_correlation.figure)

name = st.text_input("Please give me your name :")
name_length = len(name)
st.write("Your name has ",name_length,"characters")

#On peut intégrer un checkbox:
agree = st.checkbox('I agree')
if agree:
    st.write('Great!')