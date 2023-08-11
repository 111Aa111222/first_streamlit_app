import streamlit as st

st.title('My Parents New Healthy Diner')
st.header('Breakfast Menu')

st.text('🥣Omega 3 & Blueberry Oatmeal \n🥗Kale, Spinach & Rocket Smoothie \n🐔Hard-Boiled Free-Range Egg\n🥑🍞Avocado Toast')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruit_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruit_to_show = my_fruit_list.loc[fruit_selected]

# Display the table on the page.
st.dataframe(fruit_to_show)

#New Section to display fruityvice api response
st.header('Fruityvice Fruit Advice!')
fruit_choice = st.text_input('What fruit would you like information about?', 'Kiwi')
st.write('The user entered',fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)


#take the json version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#output it the screen as a table
st.dataframe(fruityvice_normalized)


import snowflake.connector

st.text("Hello from Snowflake:")

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()

st.text(my_data_row)

