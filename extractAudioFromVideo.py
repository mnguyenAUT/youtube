import cv2
import sys
import moviepy.editor as mp

# Read video clip and store all images in to Temp/Frame_xxxxx.jpg
argument = "datasets/walkVideos/How_People_Walk.mp4"

if len(sys.argv) > 1:
	argument = sys.argv[1]
    
my_clip = mp.VideoFileClip(argument)

my_clip.audio.write_audiofile(r"audio_out.mp3")