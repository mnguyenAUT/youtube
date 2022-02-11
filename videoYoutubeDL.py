import youtube_dl
from pytube import YouTube
import sys
import os

ydl_opts = {
    'format': 'bestvideo/best'
}

if __name__ == "__main__":
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        filenames = sys.argv[1]
        print (filenames)
        #ydl.download(filenames)  
        getVideo = YouTube(filenames)
        videoStream = getVideo.streams.get_highest_resolution()         
        videoStream.download()
