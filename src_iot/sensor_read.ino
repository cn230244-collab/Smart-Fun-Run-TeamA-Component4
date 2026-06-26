#define BLYNK_TEMPLATE_ID "TMPL60K0Udy-I"
#define BLYNK_TEMPLATE_NAME "SmartSync Hydration"
#define BLYNK_AUTH_TOKEN "4k8Bl4TxK5WISA4Q6dh1owbL5sSqKkX2"

#include <WiFi.h>
#include <BlynkSimpleEsp32.h>

#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

// WiFi
char ssid[] = "aidil";
char pass[] = "asd123asd";

// OLED
#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

// IR sensor
#define IR_PIN 4

int bottleCount = 0;
int maxBottle = 60;

bool lastState = HIGH;
bool notificationSent = false;

// Reset button from Blynk (V2)
BLYNK_WRITE(V2) {
  if (param.asInt() == 1) {
    bottleCount = 0;
    notificationSent = false;
    Serial.println("System Reset from Blynk");
  }
}

void setup() {
  Serial.begin(115200);

  pinMode(IR_PIN, INPUT);

  // Connect to Blynk
  Blynk.begin(BLYNK_AUTH_TOKEN, ssid, pass);

  // OLED init
  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println("OLED not found");
    while (true);
  }

  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(WHITE);

  Serial.println("System Ready...");
}

void loop() {
  Blynk.run();

  bool currentState = digitalRead(IR_PIN);

  // Detect bottle (falling edge)
  if (lastState == HIGH && currentState == LOW) {
    if (bottleCount < maxBottle) {
      bottleCount++;
      Serial.print("Bottle Count: ");
      Serial.println(bottleCount);
      delay(300); // debounce
    }
  }

  lastState = currentState;

  int remaining = maxBottle - bottleCount;

  // 🔔 Notification logic
  if (remaining <= 20 && !notificationSent) {
    Serial.println("⚠️ Triggering LOW BOTTLE notification...");
    Blynk.logEvent("low_bottle", "⚠️ Water bottles are running low!");
    notificationSent = true;
  }

  // Reset notification if refill
  if (remaining > 20) {
    notificationSent = false;
  }

  // Send to Blynk
  Blynk.virtualWrite(V0, bottleCount);
  Blynk.virtualWrite(V1, remaining);

  // OLED display
  display.clearDisplay();

  display.setCursor(0, 10);
  display.print("Hydration Counter");

  display.setCursor(0, 30);
  display.print("Given: ");
  display.print(bottleCount);

  display.setCursor(0, 45);
  display.print("Remaining: ");
  display.print(remaining);

  if (remaining <= 20) {
    display.setCursor(0, 55);
    display.print("LOW STOCK!");
  }

  display.display();
}
