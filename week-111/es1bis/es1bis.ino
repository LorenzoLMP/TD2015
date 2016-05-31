#include <Wire.h>
#define AD 0x29
byte contr;
byte stat;
void setup() {
  Serial.begin(9600);
  Wire.begin();
  //Wire.beginTransmission(AD);
  //Wire.write(0xEE);
  //Wire.endTransmission();
  Wire.beginTransmission(AD);
  Wire.write(0x80);
  Wire.write(0x03);
  Wire.endTransmission();

  Wire.beginTransmission(AD);
  Wire.write(0x8a);
  Wire.endTransmission();
  Wire.requestFrom(AD, 1);
  contr = Wire.read();
  Serial.print("serial part number: ");
  Serial.println(contr, HEX);
  delay(200);

  //Wire.beginTransmission(AD);
  
  //Wire.write(0x80);
 //Wire.endTransmission();
  //Wire.requestFrom(AD, 1);
  //stat = Wire.read();
  //Serial.print("status ");
  //Serial.print(stat, DEC);
  //delay(200);

  Wire.beginTransmission(AD);
  Wire.write(0x81);
  Wire.write(0x01);
  Wire.endTransmission();
}

void loop() {
  int c;
  byte outbuf[4];
  Wire.beginTransmission(AD);
  Wire.write(0x8C);
  Wire.endTransmission();
  c=0;
  Wire.requestFrom(AD,2);
  while(Wire.available()){
    outbuf[c++]=Wire.read();
  }
  delay(800); 
  }
 

