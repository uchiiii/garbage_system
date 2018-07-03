import datetime
import numpy as np
import cv2
import json
import serial
import sys
import time
import predict
import urllib3

#You need to change server's ip address everytime!!!!
TARGET_URL = "http://ec2-54-218-103-254.us-west-2.compute.amazonaws.com:5000/with_raspi"
ARDUINO = '/dev/ttyACM0'

def main():
    with serial.Serial(ARDUINO,9600) as ser:
        time.sleep(20)
        while True:
            #import pdb; pdb.set_trace()
            if ser.in_waiting > 0:
                ser.reset_input_buffer()
                frame = take_photo()
                #image recognition
                infer = image_recognition(frame)
                #send the int to Aruduino
                send_to_arduino(ser,infer)
                send_to_server(infer)
                ser.reset_input_buffer()
        ser.close()

def take_photo():
    cap = cv2.VideoCapture(1)
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    cap.release()
    return gray

def image_recognition(frame):
    output = predict.prd(frame)
    if(output == 3):
        infer = 'pet'
    elif(output == 2):
        infer = 'bin'
    elif(output == 1):
        infer = 'can'
    return infer

def send_to_arduino(ser,infer):
    i = 0
    if  infer == 'pet':
        i = 0
    elif infer == 'bin':
        i = 1
    elif infer == 'can':
        i = 2
    else:
        sys.stderr.write('Error occurred!')
    i = str(i)
    ser.write(i)

def send_to_server(infer):
    http = urllib3.PoolManager()
    data = {'garbage': infer}
    http.request('GET',TARGET_URL, data)

if __name__=="__main__":
    main()