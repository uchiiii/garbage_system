'''
On every occastion, 0 refers to pet(bottle), 1 bin, 2 can.
'''

from flask import Flask, render_template, request, jsonify
import datetime
import numpy as np
import cv2
import os
import sys
import json
import serial
import time, threading

#dictionary to store the current amount of garbage
garbage_amount = {'pet':0, 'bin':0, 'can':0}

#dictionary to store the total amount of garbage
total_amount = [{"2018/4": 3, "2018/5" : 8},{"2018/4": 4, "2018/5": 6},{"2018/4": 12, "2018/5": 2}]

#The class below is for the process with arduino
class Triger():
    def __init__(self):
        self.process_event = threading.Event()

        #create and start threading
        self.thread = threading.Thread(target = self.waiting)
        self.thread.start()

    def waiting(self):
        with serial.Serial('/dev/ttyACM0',9600,timeout=1) as ser:
            while True:
                if ser.in_waiting > 0:
                    frame = self.take_photo()
                    #image recognition
                    infer = self.image_recognition(frame)
                    self.add_to_dic(infer)
                    #send the int to Aruduino
                    self.send_to_arduino(ser, infer)

            ser.close()

    def take_photo(self):
        cap = cv2.VideoCapture(0)
        _, frame = cap.read()
        cap.release()
        return frame

    def image_recognition(self,frame):
        #not yet
        infer = 0
        #infer is supposed to be 'pet' or 'bin', 'can'
        return infer

    def add_to_dic(self,infer):
        if infer in garbage_amount:
            garbage_amount[infer] += 1

    def send_to_arduino(self, ser, infer):
        i = 0
        if infer == 'pet':
            i = 0
        elif infer == 'bin':
            i = 1
        elif infer == 'can':
            i = 2
        else:
            sys.stderr.write('Error occurred!')
        ser.write(i)


#below is the server setting.
app = Flask(__name__)

#th process of the top page
@app.route("/")
def put_out_num():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
        'time': timeString,
        'num_pet': garbage_amount['pet'],
        'num_bin': garbage_amount['bin'],
        'num_can': garbage_amount['can']
    }
    return render_template('main.html', **templateData)

@app.route('/reset')
def load_html():
    return render_template('reset.html')

@app.route('/draw_graph')
def reset():
    today = datetime.date.today()
    i = 0
    year_month = str(today.year) + '/' + str(today.month) 
    for item in garbage_amount.keys():
        if year_month in total_amount[i]:
            total_amount[i][year_month] += garbage_amount[item]
        else:
            total_amount[i][year_month] = garbage_amount[item]
        garbage_amount[item] = 0
    print(total_amount[0])
    #response = jsonify({ 'pet' : total_amount[0], 'bin' : total_amount[1], 'can' : total_amount[2]})
    response = jsonify(**total_amount[0])
    response.status_code = 200
    print(response)
    return response

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/location')
def loc_map():
    return render_template('/location.html')



if __name__=="__main__":
    #myThread = Triger()
    app.run(host='0.0.0.0', port=5000, debug=True)