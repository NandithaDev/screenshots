import cv2
import yt_dlp
import numpy as np
import os

ydl_opts = {
    'format': 'bestvideo+bestaudio/best',
    'merge_output_format': 'mp4',  # Ensures the final output is MP4
    'outtmpl': 'vid1.mp4',
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',  # Convert to MP4 if necessary
    }]
}

url = "https://www.youtube.com/watch?v=Zi3csr_SVKk&list=PL7lBkW4pLsIJ_hp6PFndYb3GRAA8Z4pYt"
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
