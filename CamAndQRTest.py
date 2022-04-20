#  Includes
import cv2
import os
import numpy as np

#  Globals
qrCodeDetecter = cv2.QRCodeDetector()
image = cv2.imread('/home/pi/Desktop/stackOverflowSample.png')
data, points, _ = qrCodeDetecter.detectAndDecode(image)

def sampleCamera():
	command = "libcamera-still -o FromPythonScript.jpg"
	os.system(command)

def sampleQRRead():
	if points is not None:
		nrOfPoints = points.shape[0]
		for i in range(nrOfPoints):
			next=(i+1)%nrOfPoints
			#cv2.line(image, 
			#	 tuple(points[i, :].astype('int32')), 
			#	 tuple(points[next, :].astype('int32')),
			#	 (255,0,0),
			#	 5)
			print(data)    
			cv2.imshow('image', image)
			cv2.waitKey(0)
			cv2.destroyAllWindows()
	else:
		print("QR code not detected")

sampleQRRead()
	