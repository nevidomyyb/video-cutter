import os
import streamlit as st
from moviepy.video.io.VideoFileClip import VideoFileClip
import tempfile
from datetime import timedelta
import re

def string_to_timedelta(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    # delta = timedelta(hours=hours, minutes=minutes, seconds=seconds)
    delta = (hours, minutes, seconds)
    return delta

def check_format(str):
    pattern = r'^\d{2}:\d{2}:\d{2}$'
    return re.match(pattern, str) is not None

def trim_video(video_file, start_time, end_time):
    try:
        with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as temp_file:
            temp_file.write(video_file.getvalue())
            temp_file_path = temp_file.name
            
            video = VideoFileClip(temp_file_path)
            trimmed_video = video.subclip(start_time, end_time)
            trimmed_video_path = f"{video_file.name}-cutted.mp4"
            trimmed_video.write_videofile(trimmed_video_path, codec="libx264")
            
            return trimmed_video_path
    except Exception as e:
        st.error(f"Error occurred: {str(e)}")
    
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

        start = string_to_timedelta(start)
        end = string_to_timedelta(end)
        cutted_video = trim_video(video_file, start, end)
        