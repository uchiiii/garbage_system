#include<Servo.h>

int analogPin = A3;

Servo servo1, servo2, servo3, servo4;

const int servoPin1 = 3;
const int servoPin2 = 5;
const int servoPin3 = 6;
const int servoPin4 = 11;

const int triger_val = 50;
int val = 0;

const int max_angle = 180;
const int mid_angle = 120;
const int min_angle = 0;

const int wait1 = 2000;
const int wait2 = 500;
const int wait3 = 3000;

void setup(){
	Serial.begin(9600);
	servo1.attach(servoPin1);
	servo2.attach(servoPin2);
	servo3.attach(servoPin3);
	servo4.attach(servoPin4);
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
		Serial.write(1);			
		//30秒（これはすべての制御が終わる時間）待つ
		delay(30000);
	}	

//サーボモータに関するコード
	//raspiからの入力があったとき
	if(Serial.available() > 0){
		// i = {0,1,2,3}
		int i = Serial.read();

		switch(i){
			case 0: 
				servo1.write(max_angle);
				servo2.write(max_angle);
				delay(wait1);
				servo1.write(mid_angle);
				servo2.write(mid_angle);
				delay(wait2);
				servo1.write(max_angle);
				servo2.write(max_angle);
				delay(wait1);
				servo1.write(mid_angle);
				servo2.write(mid_angle);
				delay(wait2);
				servo1.write(max_angle);
				servo2.write(max_angle);
				delay(wait3);
				servo1.write(min_angle);
				servo2.write(min_angle);

						
			case 1: 
				servo2.write(max_angle);
				servo3.write(max_angle);
				delay(wait1);
				servo2.write(mid_angle);
				servo3.write(mid_angle);
				delay(wait2);
				servo2.write(max_angle);
				servo3.write(max_angle);
				delay(wait1);
				servo2.write(mid_angle);
				servo3.write(mid_angle);
				delay(wait2);
				servo2.write(max_angle);
				servo3.write(max_angle);
				delay(wait3);
				servo2.write(min_angle);
				servo3.write(min_angle);

			
			case 2: 
				servo3.write(max_angle);
				servo4.write(max_angle);
				delay(wait1);
				servo3.write(mid_angle);
				servo4.write(mid_angle);
				delay(wait2);
				servo3.write(max_angle);
				servo4.write(max_angle);
				delay(wait1);
				servo3.write(mid_angle);
				servo4.write(mid_angle);
				delay(wait2);
				servo3.write(max_angle);
				servo4.write(max_angle);
				delay(wait3);
				servo3.write(min_angle);
				servo4.write(min_angle);
			
			case 3: 
				servo4.write(max_angle);
				servo1.write(max_angle);
				delay(wait1);
				servo4.write(mid_angle);
				servo1.write(mid_angle);
				delay(wait2);
				servo4.write(max_angle);
				servo1.write(max_angle);
				delay(wait1);
				servo4.write(mid_angle);
				servo1.write(mid_angle);
				delay(wait2);
				servo4.write(max_angle);
				servo1.write(max_angle);
				delay(wait3);
				servo4.write(min_angle);
				servo1.write(min_angle);
		}
	}
}

