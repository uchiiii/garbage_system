<<<<<<< HEAD
'''
On every occastion, 0 refers to pet(bottle), 1 bin, 2 can.
'''

from flask import Flask, render_template
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
total_amount = [{},{},{}]

#The class below is for the process with arduino
class Triger():
    def __init__(self):
        self.process_event = threading.Event()

        #create and start threading
        self.thread = threading.Thread(target = self.waiting)
        self.thread.start()

    def waiting(self):
        with serial.Serial('COM3',9600,timeout=1) as ser:
            while True:
                if ser.inwaiting()>0:
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

=======
from flask import Flask, render_template
import datetime

app = Flask(__name__)


>>>>>>> 2b6664dd254c4eab8c67502ee99bc94de407a756
#th process of the top page
@app.route("/")
def put_out_num():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
<<<<<<< HEAD
    templateData = {
        'time': timeString,
        'num_pet': garbage_amount['pet'],
        'num_bin': garbage_amount['bin'],
        'num_can': garbage_amount['can']
    }
    return render_template('main.html', **templateData)


@app.route('/reset', methods=['GET'])
def reset():
    today = datetime.date.today()
    i = 0
    year_month = str(today.year) + ' ' + str(today.month) 
    for item in garbage_amount.keys():
        if year_month in total_amount[i]:
            total_amount[i][year_month] += garbage_amount[item]
        else:
            total_amount[i][year_month] = garbage_amount[item]
        #reset
        garbage_amount[item] = 0

    total_amount_pet = total_amount[0]
    total_amount_bin = total_amount[1]
    total_amount_can = total_amount[2]

    return render_template('reset.html',total_amount_pet=total_amount_pet, total_amount_bin=total_amount_bin,total_amount_can=total_amount_can)

#def write_amount():
=======

    templateData = {
        'time': timeString;
        'num_pet':,
        'num_bin':,
        'num_cam':
    }

    return render_template('main.html', **templateData)

>>>>>>> 2b6664dd254c4eab8c67502ee99bc94de407a756



if __name__=="__main__":
<<<<<<< HEAD
    myThread = Triger()
=======
>>>>>>> 2b6664dd254c4eab8c67502ee99bc94de407a756
    app.run(host='0.0.0.0', port=80, debug=True)