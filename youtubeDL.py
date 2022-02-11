#youtube-dl PLY8dabY3aEzcDOYzi3Q5GXb5CnCbmHSdw

import youtube_dl
import sys
import os

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

if __name__ == "__main__":
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        filenames = sys.argv[1:]
        idName = 0
        if len(sys.argv) > 2:
            idName = sys.argv[2]
        else:
            idName = '0'
        number_str = str(idName)
        zero_filled_number = ""+number_str.zfill(3)+"_"
        
        #ydl.download(filenames)
        print(filenames[0])
        meta = ydl.extract_info(filenames[0], download=False)
        print(meta['title'])
        
        ydl.download([filenames[0]])
        #renameCommand = "rename \""+meta['title']+"\"* \""+zero_filled_number+meta['title']+"\"*";
        #print(renameCommand)
        
        #os.system(renameCommand)
        
        #print(zero_filled_number)
        
        #print("ffmpeg.exe -i \""+filenames[0]+"\"  -vn -ab 192k -ar 44100 -y \""+zero_filled_number+filenames[0]+".mp3\"")
        
        #os.system("ffmpeg.exe -i \""+filenames+"\"  -vn -ab 192k -ar 44100 -y \""+zero_filled_number+filenames+".mp3\"")
