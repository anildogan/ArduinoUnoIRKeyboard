
#include <IRremote.h>

int RECV_PIN = 7;

IRrecv irrecv(RECV_PIN);

decode_results results;

String past = "";
void setup()
{
  Serial.begin(9600);
  // In case the interrupt driver crashes on setup, give a clue
  // to the user what's going on.
  Serial.println("Enabling IRin");
  irrecv.enableIRIn(); // Start the receiver
  Serial.println("Enabled IRin");
  pinMode(8, OUTPUT);
}

void loop() {
  if (irrecv.decode(&results)) {
    //Commented part prints the decoded value that comes from IR remote, change the if clauses as you wish with relative to your button layout
    //Serial.println(results.value);
    
    if(results.value == 2724020415){
      Serial.println("upmouse");
      past = "upmouse";
    }
    if(results.value == 2724012255){
      Serial.println("leftmouse");
      past = "leftmouse";
    }
    if(results.value == 2724008175){
      Serial.println("downmouse");
      past = "downmouse";
    }
    if(results.value == 2724028575){
      Serial.println("rightmouse");
      past = "rightmouse";
    }
    
    if(results.value == 2724004095){
      Serial.println("kill");
      past = "kill";
    }
    if(results.value == 2724030615){
      Serial.println("mute");
      past = "mute";
    }
    if(results.value == 2724055095){
      Serial.println("vol_up");
      past = "vol_up";
    }
    if(results.value == 2724042855){
      Serial.println("vol_down");
      past = "vol_down";
    }
    if(results.value == 2724054075){
      Serial.println("previous");
      past = "previouse";
    }
    if(results.value == 2724013275){
      Serial.println("next");
      past = "next";
    }
    if(results.value == 2724046935){
      Serial.println("play");
      past = "play";
    }
    
    if(results.value == 2724037755){
      Serial.println("click");
      past = "click";
    }
    if(results.value == 2724022455){
      Serial.println("close");
      past = "close";
    }
    if(results.value == 2724004350){
      Serial.println("up");
      past = "up";
    }
    if(results.value == 2724039285){
      Serial.println("left");
      past = "left";
    }
    if(results.value == 2724049485){
      Serial.println("right");
      past = "right";
    }
    if(results.value == 2724036990){
      Serial.println("down");
      past = "down";
    }
    if(results.value == 4294967295){
      Serial.println(past);
    }
    irrecv.resume(); // Receive the next value
  }
}
