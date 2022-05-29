## Inspiration
On average, airlines lose 2 in every 1000 bags that pass through their circulation systems, which costs the aviation industry around 6 million USD a year.  Meanwhile, passengers feel a sense of uncertainty in the status of their luggage when waiting to pick up their luggage from the airport terminal.  Our product, My Luggage Handler (MLH), can help benefit the interests of both parties by improving trust between customers and aviation companies.

## What it does
There are several functions that have been integrated for backend and frontend use. For the front end, we used a CSS file to display two pages: a login page and an information page. To log into the system, a phone number is entered and the database retrieves information associated with the traveler, including their name, start and end destinations, and luggage status and ID.
<br>
For the backend, an Arduino is used to scan the RFID chip, representing a luggage tag that acts like a chip.  After the chip is scanned, a text is sent to the traveler’s phone to notify them that their luggage is ready to be picked up.  After all the user’s luggage is picked up, they receive a text notifying them of the event.  The user’s luggage status is updated in the database when the chip is scanned during the process.

## How we built it
The frontend was built using HTML, CSS, and Javascript.  First, the HTML is written to create a general format of the web app and CSS is used to format the contents.  Then, Javascript is used to transition the interface from the login page to display the information page.  The two pages of the interface are attached in the project media in their respective order.
<br>
For the hardware, we decided to use an RFID scanner (Mifare RC522 RF IC Card Sensor Module + S50 Blank Card + Key Ring) to simulate a luggage check in with a tag. Using the arduino IDE to output to the com3 terminal, as well as the python package PySerial to read the serial port of the scanned chip. Then, we used the get_ID() function to decode the output information and return a hexadecimal string of the ID. The ID could then be attributed to the user, so that a scan of the same tag at the desired Airport Terminal will send a text via Twilio notifying them with time and location data. 

## Challenges we ran into
For the hardware, we only had an Arduino Mega 2560. While this is great for most larger sensor projects, it can be a pain to set up. This is because guides showing how to use certain sensors use the standard Arduino pinout. Therefore, we had to find the Pin Equivalents to correctly transfer the data on my different board. 
<br>
Once the correct pinout was completed, there were several version errors. Pins were not pushed in correctly, giving false voltage outputs which lead to scan failures. Furthermore, The libraries used to read RFID data easily (_<SPI.h>_  and  _<MFRC522.h>_) did not have as much documentation and troubleshooting as more popular forums. 
<br>
We originally planned to create a database with Firebase for the MLH web app, but technical difficulties in the installation process led us to abandon setting up the database.  The first step in setting up a Firebase database was to install it, and we all spent several hours attempting to install it due to failure in setting up a module.  In the future, we will use a different database service to create one.  The repository containing the database files is located here: [link](https://github.com/aesmi/mlh-2022-rn-app).
The database was intended to connect the frontend to backend, and abandoning it involved two different deliverables, the backend and the UI for the web app, as linked here: [link](https://mx.myluggagehandler.tech/).

## What we learned
This project integrated several different parts of developing a device, making it an excellent opportunity to learn how a team environment would work, and how hardware interacts with software in real time. Additionally, this event also taught us how the backend, database, and frontend all interact with each other, although we struggled in integrating Firebase.
<br>
It also taught us to work efficiently and work with people from different time zones as Andy is in Eastern Australia and Noah, Jack, and Helen are in the CST time zone, thus putting us 13 hours apart.  We learned to be considerate of each others’ time constraints and adapt to sudden changes in plans.  Overall, we became more familiar with topics that we were once unfamiliar with, both on the hardware and software side.  

## What's next for MLH: My Luggage Handler
For future implementation, our primary goal would be to make sure the backend, frontend, and the database can all work together. Another future implementation would be to implement hashing for the tag IDs, so that it would add that extra layer of security that airports deem necessary for their security expectations.  We also plan to adjust the media query for better display on mobile devices.

