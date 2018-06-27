#include<Servo.h>

int analogPin = A0;

Servo servo1, servo2, servo3, servo4;

const int servoPin1 = 3;
const int servoPin2 = 5;
const int servoPin3 = 6;
const int servoPin4 = 9;

const int triger_val = 80;
int val = 0;

const int max_angle1 = 180;
const int mid_angle1 = 120;
const int min_angle1 = 0;
const int max_angle2 = 0;
const int mid_angle2 = 60;
const int min_angle2 = 180;

const int wait1 = 2000;
const int wait2 = 500;
const int wait3 = 3000;

void setup(){
	Serial.begin(9600);
	servo1.attach(servoPin1);
	servo2.attach(servoPin2);
	servo3.attach(servoPin3);
	servo4.attach(servoPin4);
	servo1.write(min_angle1);
	servo2.write(min_angle2);
	servo3.write(min_angle1);
	servo4.write(min_angle2);
}


void loop(){
//圧力センサに関するコード
	//電圧を読みとる	
	val = analogRead(analogPin);
	
	//値の表示
	//Serial.println(val);

	//電圧が一定以上の時
	if(val > triger_val){
		//int 1を送る
		delay(1000);
		Serial.write('1');
                delay(100);		
		while(true){
			
			//サーボモータに関するコード
			//raspiからの入力があったとき
			if(Serial.available() > 0){
		// i = {0,1,2,3}
				int i = Serial.read()-(int)'0';
                             
				switch(i){
					case 0: 
						servo1.write(max_angle1);
						servo2.write(max_angle2);
						delay(wait1);
						servo1.write(mid_angle1);
						servo2.write(mid_angle2);
						delay(wait2);
						servo1.write(max_angle1);
						servo2.write(max_angle2);
						delay(wait1);
						servo1.write(mid_angle1);
						servo2.write(mid_angle2);
						delay(wait2);
						servo1.write(max_angle1);
						servo2.write(max_angle2);
						delay(wait3);
						servo1.write(min_angle1);
						servo2.write(min_angle2);
						break;
						
					case 1: 
						servo2.write(max_angle2);
						servo3.write(max_angle1);
						delay(wait1);
						servo2.write(mid_angle2);
						servo3.write(mid_angle1);
						delay(wait2);
						servo2.write(max_angle2);
						servo3.write(max_angle1);
						delay(wait1);
						servo2.write(mid_angle2);
						servo3.write(mid_angle1);
						delay(wait2);
						servo2.write(max_angle2);
						servo3.write(max_angle1);
						delay(wait3);
						servo2.write(min_angle2);
						servo3.write(min_angle1);
						break;
					
					case 2: 
						servo3.write(max_angle1);
						servo4.write(max_angle2);
						delay(wait1);
						servo3.write(mid_angle1);
						servo4.write(mid_angle2);
						delay(wait2);
						servo3.write(max_angle1);
						servo4.write(max_angle2);
						delay(wait1);
						servo3.write(mid_angle1);
						servo4.write(mid_angle2);
						delay(wait2);
						servo3.write(max_angle1);
						servo4.write(max_angle2);
						delay(wait3);
						servo3.write(min_angle1);
						servo4.write(min_angle2);
						break;

					default: 
						servo4.write(max_angle2);
						servo1.write(max_angle1);
						delay(wait1);
						servo4.write(mid_angle2);
						servo1.write(mid_angle1);
						delay(wait2);
						servo4.write(max_angle2);
						servo1.write(max_angle1);
						delay(wait1);
						servo4.write(mid_angle2);
						servo1.write(mid_angle1);
						delay(wait2);
						servo4.write(max_angle2);
						servo1.write(max_angle1);
						delay(wait3);
						servo4.write(min_angle2);
						servo1.write(min_angle1);
						break;
				}
				break;
			}
		}
	}		
}

