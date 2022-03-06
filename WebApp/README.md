#  Introduction  
This is the sub-directory to hold the web application components  

#  Objective  
The purpose of this web application is to meet the demands and requirements of Group 10's Soil Tester 1.0  
1)  The web application shall display an interactive format for the user to see plant detail
2)  The web application will display the data file containing information on moisture level  
3)  The web appication shall trigger the robot to start moving and collect data
4)  Read the data file generated from the Raspberry Pi after data is processed

# Apache2  
The web application is hosted through the device's localhost address on Port 80 using Apache2's service  

# Javascript
The javascript used for the SoilTester Data page reads from a file named "dataFile.txt" which will eventually be generated from the Python code while the SoilTester Device is actively generating data from the Moisture Sensor and QR Code Reader.  
