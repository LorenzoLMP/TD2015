/*
  accende e spegne un led messo sul PIN  NNN
 */
 
int outp = 8;   // pin

void setup() {                
  // scegli il pin e lo configura come output
  pinMode(outp, OUTPUT);     
}

void loop() {
  digitalWrite(outp, HIGH);   // accende
 // delay(random(10,50));              // aspetta 
  delay(1000);
  digitalWrite(outp, LOW);    // spegne
  delay(random(20,100));              // aspetta
}
