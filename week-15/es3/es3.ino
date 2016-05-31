char a='@';
char b='(';
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.print(a);
  delay(3);
  Serial.print(b);
  delay(100);
}
