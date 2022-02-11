# Python program to illustrate the concept
# of threading
# importing the threading module
import threading
import youtube_dl
import sys
import os

def task(string, ID):	
	#print("download: {}".format(string))
	print("downloading file {}: {}".format(count, string.strip()))
	stringCommand = "youtubeDL.py https://www.youtube.com/watch?v=" + string.strip() +" "+str(ID)
	print(str(ID)+": \n")
	print(stringCommand)
	os.system(stringCommand)

if __name__ == "__main__":

	print("Usage:")
	print("python downloadPlayListYouTubeAudio.py playlist.txt")
	print("A file called playlist.txt needed, to create this file, call playListYouTube.py")
	print("Enjoy!")
	filenames = sys.argv[1]    
	file1 = open(filenames, 'r')
	count = 0
	fileName = []
	 
	while True:
		count += 1  
		line = file1.readline()     
		fileName.append(line)
		if not line:
			break
		#print("downloading file {}: {}".format(count, line.strip()))
		#stringCommand = "youtubeDL.py https://www.youtube.com/watch?v=" + line.strip()
		#print(stringCommand)
		#os.system(stringCommand)
	 
	file1.close()

	# creating thread
	t1 = []
	RANGE = count
	
	for x in range(RANGE):		
		t = threading.Thread(target=task, args=(fileName[x], x))
		t1.append(t)
	
	for x in range(RANGE):		
		t1[x].start()

	for x in range(RANGE):		
		t1[x].join()        

	# both threads completely executed
	print("Done!")
