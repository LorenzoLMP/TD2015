#include <Wire.h>
#define AD 0x48
#define BC 0x49


byte outbuf[2];
byte outpippo[2];
void setup() {
  Serial.begin(9600);
  Wire.begin();
  Wire.beginTransmission(AD);
  Wire.write(0xEE);
  Wire.endTransmission();
  Wire.beginTransmission(BC);
  Wire.write(0xEE);
  Wire.endTransmission();
}

void loop() {
 lettura(AD);
 delay(100);
 lettura(BC);
 delay(1000);
 
 }


void lettura(char ind){
 double thr;
 int nb=2, c;
 byte data, data2;
 Wire.beginTransmission(ind);
 Wire.write(0xAA);
 Wire.endTransmission();
 Wire.requestFrom(ind,nb);
 delay(10);
 c=0;
 while(c<nb) {
  outbuf[c] = Wire.read();
  c=++c;
 }
 data=outbuf[0];
 data2=outbuf[1];
 data2 = data2>>3;
 thr=int(data)+int(data2)*0.03125;
 Serial.println(thr,2);  
}
