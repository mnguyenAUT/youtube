import youtube_dl
import sys
import os

if __name__ == "__main__":
    print("Usage:")
    print("python playListYouTube.py PLY8dabY3aEzcDOYzi3Q5GXb5CnCbmHSdw")
    print("A file called playlist.txt will be created")
    print("Enjoy!")
    filenames = sys.argv[1]
    stringCommand = "youtube-dl --get-id "+sys.argv[1]+" > playlist.txt"
    print(stringCommand)
    os.system(stringCommand)

