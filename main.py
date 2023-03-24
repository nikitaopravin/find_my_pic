import streamlit as st
import random
import os
import clip
from funcs.get_similarity import get_similarity_score, create_filelist, load_embeddings, find_matches
from funcs.fiass_similaruty import load_embeddings, encode_text, find_matches_fiass
import torch.nn.functional as F
import pandas as pd

device = 'cpu'
model_path = "weights/ViT-B-32.pt"

model, preprocess = clip.load('ViT-B/32', device)

file_name = create_filelist('img')
features = load_embeddings('embeddings/emb_images_5000.npy')
df = pd.read_csv('data/results.csv')

random_queries = ['friends playing cards', 'rock band playing on guitars', 'policeman cross the road', 
                  'sleeping kids', 'football team playing on the grass' , 'learning programming'
                  ]

st.header('Find my pic!')

request = st.text_input('Write a description of the picture', ' Two people at the photo')

img_count = st.slider('How much pic you need?', 4, 8, 6, 2)


matches = find_matches_fiass(features, request, file_name, img_count)
row1, row2 = st.columns(2)
    
if st.button('Find!'):

    selected_filenames = matches

    for i in range(int(img_count/2)):
        filename = selected_filenames[i]
        img_path = filename
        img_discription = df[df['image_name'] == filename.split('/')[1]]['comment'].iloc[0]
        with row1:
            st.image(img_path, width=300, caption=img_discription)

    # display next 3 images in the second row
    for i in range(int(img_count/2), img_count):
        filename = selected_filenames[i]
        img_path = filename
        img_discription = df[df['image_name'] == filename.split('/')[1]]['comment'].iloc[0]
        with row2:
            st.image(img_path, width=300, caption=img_discription)