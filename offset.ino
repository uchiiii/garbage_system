
int analogPin = 221;

const int triger_val = 50;
int val = 0;

void setup(){
	Serial.begin(9600);
}


void loop(){
	//電圧を読みとる	
	val = analogRead(analogPin);
	
	//値の表示
	//Serial.println(val);

	//電圧が一定以上の時
	if(val > triger_val){
		//int 1を送る
		Serial.write(1);			
		//30秒待つ
		delay(30000);
	}	
}
