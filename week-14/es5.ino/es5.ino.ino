void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.println("inizializzazione");
  analogReference(DEFAULT);
 
}

void loop() {
  // put your main code here, to run repeatedly:
  int sensorValue = analogRead(0);
  float x = sensorValue*5.04/1023;
  Serial.print(sensorValue, DEC);
  Serial.print("\t");
  Serial.println(x, 4);
  //delay(125);
}



