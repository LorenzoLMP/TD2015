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

  Wire.beginTransmission(AD);
  Wire.write(0x81);
  Wire.write(0x12);//402 ms, gain = 16x
  Wire.endTransmission();
}

void loop() {
  byte outbuf[4];
  long ch0, ch1;
  double rat, lux, r4;
  int c;
  Wire.beginTransmission(AD);
  Wire.write(0x8C);
  Wire.endTransmission();
  c=0;
  Wire.requestFrom(AD,4);
  while(Wire.available()){
    outbuf[c++]=Wire.read();
  }

  ch0 = outbuf[1];
  ch0 <<= 8;
  ch0 += outbuf[0];

  ch1 = outbuf[3];
  ch1 <<= 8;
  ch1 += outbuf[2];

  rat = ch1;
  rat = rat/ch0;
  if (rat <= 0.50){
    r4 = pow(rat,1.4);
    lux = 0.0304*ch0-0.062*ch0*r4;
  }
  else if (0.5 < rat <= 0.61){
    lux = 0.0224*ch0-0.031*ch1;
  }
   else if (0.61 < rat <= 0.80){
    lux = 0.0128*ch0-0.0153*ch1;
  }
   else if (0.8 < rat <= 1.30){
    lux = 0.00146*ch0-0.00112*ch1;
  }
   else {
    lux = 0;
  }
  if (ch1 == 65535 || ch0== 65535){
    lux = 9001;
  }
  Serial.print(ch0, HEX);
  Serial.print(" ");
  Serial.print(ch1, HEX);
  Serial.print(" ");
  Serial.print(rat, 4);
  Serial.print(" ");
  Serial.println(lux, 1);
  delay(800);
  
}
