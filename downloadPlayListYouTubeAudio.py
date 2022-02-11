import youtube_dl
import sys
import os

if __name__ == "__main__":
    print("Usage:")
    print("python downloadPlayListYouTubeAudio.py playlist.txt")
    print("A file called playlist.txt needed, to create this file, call playListYouTube.py")
    print("Enjoy!")
    filenames = sys.argv[1]    
    file1 = open(filenames, 'r')
    count = 0
     
    while True:
        count += 1  
        line = file1.readline()     
        if not line:
            break
        print("downloading file {}: {}".format(count, line.strip()))
        stringCommand = "youtubeDL.py https://www.youtube.com/watch?v=" + line.strip()
        print(stringCommand)
        os.system(stringCommand)
     
    file1.close()

