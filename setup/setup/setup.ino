#include <IRremote.h>

#define RECEIVER_PIN 8

IRrecv receiver(RECEIVER_PIN); 
decode_results output;
 
void setup()
{
  Serial.begin(9600);
  receiver.enableIRIn();  
}
 
void loop() {
  if (receiver.decode(&output)) {
    unsigned int value = output.value;
    Serial.println(value); 
    receiver.resume(); 
  }

  delay(1000);
}
