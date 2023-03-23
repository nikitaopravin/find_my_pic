import streamlit as st

st.header('Find my pic!')

query = st.text_input('Write a description of the picture', ' Two people in the photo')
st.button('Find!')

imges = ['https://static.streamlit.io/examples/cat.jpg', 
         'https://static.streamlit.io/examples/owl.jpg',
         'https://static.streamlit.io/examples/dog.jpg',
         'https://static.streamlit.io/examples/cat.jpg',
         'https://static.streamlit.io/examples/cat.jpg', 
         'https://static.streamlit.io/examples/owl.jpg']

row_n = int(st.slider('How much pic yoou need?', 2, 6, 4, 2) / 2)

n = 0
for i in range(row_n):
    for col in st.columns(2):
        col.image(imges[n], caption='Sunrise by the mountains')
        n += 1

import os

directories = os.system('df -H')
print(directories)