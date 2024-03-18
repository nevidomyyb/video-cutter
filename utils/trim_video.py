import tempfile
from moviepy.video.io.VideoFileClip import VideoFileClip
import streamlit as st 

def trim_video(video_file, start_time, end_time):
    try:
        with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as temp_file:
            temp_file.write(video_file.getvalue())
            temp_file_path = temp_file.name
            
            video = VideoFileClip(temp_file_path)
            trimmed_video = video.subclip(start_time, end_time)
            trimmed_video_path = f"cutted/{video_file.name}-cutted.mp4"
            trimmed_video.write_videofile(trimmed_video_path, codec="libx264")
            
            return trimmed_video_path
    except Exception as e:
        st.error(f"Error occurred: {str(e)}")