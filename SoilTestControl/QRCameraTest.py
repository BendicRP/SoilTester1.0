from picamera import picamera
from time import sleep
from PIL import Image
import zbarlight

camera = PiCamera()
while True:
    camera.start_preview()
    sleep(5)
    camera.capture('/home/pi/Desktop/qr.png')
    camera.stop_preview()
    file_path = '/home/pi/Desktop/qr.png'
    with open(file_path, 'rb') as image_file:
        image = Image.open(image_file)
        image.load()
    sleep(5)
    codes = zbarlight.scan_codes(['qrcode'], image)
    print('QR codes: %s' % codes)