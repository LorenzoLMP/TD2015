
int outpin = 8 ;  // numero piede
long ritardo1 =2000 ; 
long ritardo2 =200 ;


void setup(){
   pinMode(outpin,OUTPUT);
}

void loop(){
   digitalWrite(outpin, HIGH);
   delay (ritardo1);
   digitalWrite(outpin, LOW);
  delay (ritardo2);
}

