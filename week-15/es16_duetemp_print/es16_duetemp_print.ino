#include <Wire.h>
#define AD 0x48
#define BC 0x49


byte outbuf[2];
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
 Serial.print(lettura(AD, 3, 0.03125),2);
 Serial.print("\t");
 Serial.println(lettura(BC, 7, 0.5),2);
 delay(1000);
 }


double lettura(char ind, int num, float delta){
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
 data2 = data2>>num;
 thr=int(data)+int(data2)*delta;
 return thr;  
}
