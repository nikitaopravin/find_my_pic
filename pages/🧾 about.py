import streamlit as st

st.image('data/logo.png', width=400)

st.header('How it works?')

st.write("""
        What's under the hood:  
        - it using image encoder and text encoder from pretrained 'CLIP' model
        - have 30k pic and their embedded representation
        - use faiss for faster working

        Working algorithm:
        1. User input text
        2. With text encoder, it converts to embedded representation
        3. Faiss searching matches between embedded text and embedded images
        4. Taking best n matches
        5. Show it to user
        """)
st.image('data/sheme.PNG')

st.markdown("#### Telegram Bot:")
st.write("""
        Text is sent to the input of the telegram bot, and in response, the user receives photos that best match the description
        """)
st.image('data/telegram.png')



        