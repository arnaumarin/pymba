int x;
void setup() {
  Serial.begin(9600);
  Serial.setTimeout(1);
  while (!Serial.available());
  Serial.println("<Arduino is ready>");
  Serial.println("<Enter one more number to start recording, please>");
  Serial.print(55);
  //delay 1min to give time the camera to fully setup and record
  delay(60000);
}
void loop() {
}