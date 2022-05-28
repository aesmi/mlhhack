
// ARDUINO 2650 MEGA PINOUT
// RST_PIN 5
// SDA     53
// SCK     52
// MOSI    51
// MISO    50
// IRQ     NA/
// GND     GND
// 3.3V    3.3V

// template from MFRC22 Library
#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN         5          // Pinout set to Arduino 2650 - MEGA specific
#define SS_PIN          53         

MFRC522 mfrc522(SS_PIN, RST_PIN);  // Create MFRC522 instance

void setup() {
	Serial.begin(9600);		// Initialize communication with COM3 
	while (!Serial);		// 
	SPI.begin();			// Initialize SPI bus
	mfrc522.PCD_Init();		// Initialize MFRC522
	delay(4);				// Delay of 4ms, for workability/code consistenty
	mfrc522.PCD_DumpVersionToSerial();	// Show details of PCD - MFRC522 Card Reader details
	//Serial.println(F("Scan PICC to see UID, SAK, type, and data blocks..."));
}

void loop() {
	
	// Resets loop if no card detected. Allows Scanner to "idle"
	if ( ! mfrc522.PICC_IsNewCardPresent()) {
		return;
	}

	// Pick a card, any card
	if ( ! mfrc522.PICC_ReadCardSerial()) {
		return;
	}

	// Send Luggage ID info to COM3 SERIAL PORT
	mfrc522.PICC_DumpDetailsToSerial(&(mfrc522.uid));
}