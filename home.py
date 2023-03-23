import streamlit as st
import pandas as pd
import random
import os

ten_pic_names = os.listdir('data/ten_pics/')
df = pd.read_csv('data/results.csv')

st.header('Find my pic!')

query = st.text_input('Write a description of the picture', ' Two people at the photo')
st.button('Find!')

img_count = st.slider('How much pic you need?', 2, 10, 4, 2)

rand_ind = random.sample(range(len(ten_pic_names)), img_count)
n = 0
for i in range(int(img_count / 2)):
    for col in st.columns(2):
        img_name = ten_pic_names[rand_ind[n]]
        img_discription = df[df['image_name'] == img_name]['comment'].iloc[0]
        col.image(f'data/ten_pics/{img_name}', caption=img_discription)
        n += 1