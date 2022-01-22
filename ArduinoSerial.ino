
void setup() {
  Serial.begin(115200);
  pinMode(13, OUTPUT);
}

void loop() {
  if (Serial.available()>0){
    int dado = Serial.read();
    if (dado == '1'){
      digitalWrite(13, HIGH);
    }
    else if (dado == '0'){
      digitalWrite(13, LOW);
    }
  }
}
