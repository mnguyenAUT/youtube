from moviepy.editor import *
videoclip = VideoFileClip("video_out.avi")
audioclip = AudioFileClip("audio_out.mp3")

new_audioclip = CompositeAudioClip([audioclip])
videoclip.audio = new_audioclip
videoclip.write_videofile("video_out_with_sound.mp4")