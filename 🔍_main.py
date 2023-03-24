import streamlit as st
import clip
from funcs.fiass_similaruty import load_embeddings, find_matches_fiass, create_filelist
import pandas as pd

model, preprocess = clip.load('ViT-B/32', device='cpu')

file_names = create_filelist('data/flickr30k_images')
features = load_embeddings('embeddings/emb_images_30k.npy')
df = pd.read_csv('data/results.csv')

st.image('data/logo.png', width=400)
request = st.text_input('Write a description of the pic', 'Data science')
img_count = st.selectbox('How many pic do you need?',(4, 8, 12, 16, 20, 30, 40, 50))
st.button('Find!')

matches = find_matches_fiass(features, request, file_names, img_count)
n = 0
for i in range(int(img_count / 2)):
    for col in st.columns(2):
        img_name = matches[n].split('\\')[1]
        img_discription = df[df['image_name'] == img_name]['comment'].iloc[0]
        col.image(f'data/flickr30k_images/{img_name}', caption=img_discription)
        n += 1