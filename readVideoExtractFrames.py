import cv2
import sys

# Read video clip and store all images in to Temp/Frame_xxxxx.jpg
argument = "datasets/walkVideos/How_People_Walk.mp4"

if len(sys.argv) > 1:
	argument = sys.argv[1]
    
# Opens the inbuilt camera of laptop to capture video.

i = 0
cap = cv2.VideoCapture(argument)
while(cap.isOpened()):
	ret, frame = cap.read()
	number_str = str(i)
	zero_filled_number = ""+number_str.zfill(5)
	
	# This condition prevents from infinite looping
	# incase video ends.
	if ret == False:
		break
	
	# Save Frame by Frame into disk using imwrite method
	cv2.imshow("frame", frame)
	k = cv2.waitKey(1)
	if k==27:    # Esc key to stop
		break
	cv2.imwrite('Temp/Frame_'+str(zero_filled_number)+'.jpg', frame)
	i += 1

cap.release()
cv2.destroyAllWindows()
