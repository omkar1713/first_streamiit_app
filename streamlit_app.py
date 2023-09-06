import streamlit
streamlit.title('Hello streamlit')
streamlit.header('Hello regular streamlit')
streamlit.text('Hello small streamlit')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
