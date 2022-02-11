# Python program to illustrate the concept
# of threading
# importing the threading module
import threading

def task(num):	
	print("task: {}".format(num))

if __name__ == "__main__":
	# creating thread
	t1 = []
	RANGE = 10
	
	for x in range(RANGE):
		#print(x)
		t = threading.Thread(target=task, args=(10,))
		t1.append(t)
	
	for x in range(RANGE):
		#print(x)        
		t1[x].start()

	for x in range(RANGE):
		#print(x)       
		t1[x].join()        

	# both threads completely executed
	print("Done!")
