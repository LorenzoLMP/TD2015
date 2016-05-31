#include <Wire.h>
#define AD 0x29
byte outbuf[1];
byte contr[1];
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
}

void loop() {
  int nb=1,c, da=1, f;
  //Wire.beginTransmission(AD);
  //Wire.write(0xAA);
  //Wire.endTransmission();


  
  //Wire.beginTransmission(0x8A);
  //Wire.requestFrom(0x8A, nb);
  //Wire.endTransmission();
  //delay(10);
  //c = 0;
  //while(c<nb) {
  //  outbuf[c] = Wire.read();
  //  c = ++c;
  //}
  //Serial.println(int(outbuf[1]));
  Wire.beginTransmission(AD);
  Wire.write(0x80);
  Wire.endTransmission();
  Wire.requestFrom(0x80, da);
  delay(10);
  f = 0;
  while(f<da) {
    contr[f] = Wire.read();
    f = ++f;
  }
  Serial.println(int(contr[1]));
  //Serial.println(contr[2]);
  //Serial.print(outbuf[2]);
  //Serial.println(outbuf[3]);
 }

