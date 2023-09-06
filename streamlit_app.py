import streamlit
streamlit.title('Hello streamlit')
streamlit.header('Hello regular streamlit')
streamlit.text('Hello small streamlit')

streamlit.title('Build your own fruit smoothie')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruits_list.loc[fruits_selected] 

# Display the table on the page.
streamlit.dataframe(fruits_to_show)
