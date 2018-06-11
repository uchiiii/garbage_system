import cv2
import time 
import sys
import os


def make_file(dirc_path):    
	#file_path = os.path.dirname(filename)

	#if there isnt a directory
	if not os.path.exists(dirc_path):
		os.makedirs(dirc_path)


def main():
	#command line parameters
	argv = sys.argv
	argc = len(argv)
	
	#error on the shortage of the parameters
	if(argc != 4):
		print('Usage: python %s path-to-directory  number start-point'  %argv[0])
		quit()

	#make a directory if there isn't 
	make_file(argv[1])

	#take pictures
	for i in range(int(argv[2])):

		#sleep for 2 sec
		time.sleep(2)			

		file_number = int(argv[3]) + i

		filename = "pic" + str(file_number) + ".pmg"
		filepath = argv[1] + "/" + filename
 		
		c = cv2.VideoCapture(0)
		r, img = c.read()
		cv2.imwrite(filepath, img)

	print('DONE')

if __name__ == '__main__':
	main()
