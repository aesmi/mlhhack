import serial

file = open("twilio-info.json")
data = json.load(file)

SID = data["SID"]
TOKEN = data["TOKEN"]
twilioNum = data["Phone-no"]

client = Client(SID, TOKEN)

# Arduino code
# connect to serial port, to read sensor
# sensor -> arduino (COM3) -> python
serialcomm = serial.Serial("COM3",9600)
serialcomm.timeout = 1






def get_ID() -> str:
    # search for ID until acquired
    ID_Aqcuired = False
    ID = None

    while ID_Aqcuired == False:
        # read COM3 data received in ascii
        # line by line
        g = serialcomm.readline().decode("ascii")
        # print(g[0:9])
        # print("Card UID:")
        # Card UID: (ID is the rest of the line)
        if g[0:9] == "Card UID:":
            # print(g[10:])
            ID = g[10:].replace(" ","")
            ID_Aqcuired = True
    return ID
# output function

luggageID = get_ID()
# print(luggageID)
serialcomm.close()

# Function to notify user their luggage is on the conveyer belt
def cNotif(phoneNo, luggageID, statNo): #Phone number, luggage ID, Station number
    content = "Your luggage with ID " + luggageID + " is ready for pickup at " + statNo
    message = client.messages.create(
        to = phoneNo, #Write number here
        from_ = twilioNum, #Insert Twilio number
        body = content
    )
    return


# Function to confirm to users all their luggage has been scan
def pNotif(phoneNo, statNo): #Phone number, Station number
    now = datetime.datetime.now()
    tInfo = now.strftime("%b-%d-%Y %H:%M:%S")

    message = client.messages.create(
        to = phoneNo, #Write number here
        from_ = twilioNum, #Insert Twilio number
        body = "Your luggage has been picked up from " + statNo + " at " + tInfo
    )
    return

