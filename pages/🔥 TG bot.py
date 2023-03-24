import streamlit as st

DEFAULT_WIDTH = 40
VIDEO_DATA =  open('data/video.mp4', 'rb')
st.set_page_config(layout="wide")
st.markdown('## TelegramBot : Image search by request!')
st.markdown('## @Clip_project_bot')
st.image('data/photo.jpg', width=120)
st.markdown('### Example:')
width = st.sidebar.slider(
    label="Width", min_value=0, max_value=100, value=DEFAULT_WIDTH, format="%d%%"
)
width = max(width, 0.01)
side = max((100 - width) / 2, 0.01)
_, container, _ = st.columns([side, width, side])
container.video(data=VIDEO_DATA)