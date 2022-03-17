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

# g10WebStart.sh
As the developer should be programming on their local device, this may affect their ability to interface with the directory `/var/www/html/` so a Starter script is created for the developer to integrate changes **outside** the Apache2 directory.  

Whenever changes are made within the `SoilTester.10/WebApp/html/` working repository, the g10WebStart.sh bash script will copy those changes over respectively to the Apache2 service folders.  This is really just a tool to help develop and is by no means necessary; however, it does lightly assist with setting up the system with Apache2.  
