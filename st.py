import streamlit as st
from utils.string_to_acceptable_list import string_to_acceptable_list
from utils.trim_video import trim_video
from utils.check_format import check_format    

st.info("Currently the server is not dealing with larger videos.", icon="🚨")
video_file = st.file_uploader("Select a video", ['mp4',], False)
if video_file:
    st.video(video_file, "video/mp4", 0)
    col1, col2 = st.columns(2)
    with col1:
        start = st.text_input("Start", max_chars=8)
    with col2:
        end = st.text_input("End", max_chars=8)
    r1 = check_format(start)
    r2 = check_format(end)
    if st.button("Trim", disabled=not (r1 and r2)):
        start = string_to_acceptable_list(start)
        end = string_to_acceptable_list(end)
        with st.spinner(text="Download will be available after this process ends"):
            cutted_video = trim_video(video_file, start, end)
        if cutted_video:
            with open(cutted_video, "rb") as f:
                st.download_button("Download", f, file_name="saida.mp4", mime='video/mp4')   
                
    
