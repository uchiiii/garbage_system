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
import predict

#dictionary to store the current amount of garbage
garbage_amount = {'pet':0, 'bin':0, 'can':0}

#dictionary to store the total amount of garbage
total_amount = [{ "2018/4": 3, "2018/5" : 8},{"2018/4": 4, "2018/5": 6},{"2018/4": 12, "2018/5": 2}]

#dictionary to store the name, location of the garbage you've set up.
loc_gar = {'id': 0,  'name': 'ryosuke garbage', 'lat': 35.658581, 'lng': 139.745433} 

#The class below is for the process with arduino
class Triger():
    def __init__(self):
        self.process_event = threading.Event()

        #create and start threading
        self.thread = threading.Thread(target = self.waiting)
        self.thread.start()

    def waiting(self):
        with serial.Serial('/dev/ttyACM1',9600,timeout=1) as ser:
            ser.reset_input_buffer()
            while True:
                if ser.in_waiting > 0:
                    c = ser.readline()
                    frame = self.take_photo()
                    print(frame)
                    #image recognition
                    infer = self.image_recognition(frame)
                    self.add_to_dic(infer)
                    #send the int to Aruduino
                    self.send_to_arduino(ser, infer)
                    
            ser.close()

    def take_photo(self):
        cap = cv2.VideoCapture(1)
        _, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        cap.release()
        return gray

    def image_recognition(self,frame):
        output = predict.prd(frame)
        if(output == 3):
            infer = 'pet'
        elif(output == 2):
            infer = 'bin'
        elif(output == 1):
            infer = 'can'
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
        i = str(i)
        ser.write(i)


#below is the server setting.
app = Flask(__name__)

#th process of the top page
@app.route('/')
def home():
    return render_template('main.html')

'''
@app.route('/gar_status/<int:gar_num>')
def put_out_num(gar_num):
    gar_name 
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    #need the data srtucture to be changed 
    templateData = {
        'time': timeString,
        'num_pet': garbage_amount['pet'],
        'num_bin': garbage_amount['bin'],
        'num_can': garbage_amount['can']
    }
    return render_template('main.html', **templateData)
'''


@app.route('/reset/<int:gar_id>')
def reset(gar_id):
    today = datetime.date.today()
    i = 0
    year_month = str(today.year) + '/' + str(today.month) 
    for item in garbage_amount.keys():
        if year_month in total_amount[i]:
            total_amount[i][year_month] += garbage_amount[item]
        else:
            total_amount[i][year_month] = garbage_amount[item]
        garbage_amount[item] = 0
        i += 1
    data = { 'pet_amount' : total_amount[0], 'bin_amount' : total_amount[1], 'can_amount' : total_amount[2] }
    response = jsonify(data)
    return response


@app.route('/draw_table')
def table_data():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
        'time': timeString,
        'num_pet': garbage_amount['pet'],
        'num_bin': garbage_amount['bin'],
        'num_can': garbage_amount['can']
    }
    response = jsonify(templateData)
    return response

@app.route('/draw_graph')
def graph_data():
    data = { 'pet_amount' : total_amount[0], 'bin_amount' : total_amount[1], 'can_amount' : total_amount[2] }
    response = jsonify(data)
    return response

@app.route('/personal/<int:gar_id>')
def load_html(gar_id):
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
        'name': 'keisu_garbage',
        'time': timeString,
        'num_pet': garbage_amount['pet'],
        'num_bin': garbage_amount['bin'],
        'num_can': garbage_amount['can']
    }
    return render_template('personal.html',**templateData)

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/send_loc')
def send_loc():
    response = jsonify(loc_gar)
    return response


if __name__=="__main__":
    #myThread = Triger()
    app.run(host='0.0.0.0', port=5000, debug=True)