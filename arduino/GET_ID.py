import serial

# connect to serial port, to read sensor
# sensor -> arduino (COM3) -> python
serialcomm = serial.Serial("COM3",9600)
serialcomm.timeout = 1


def get_ID() -> str:
    # search for ID until acquired
    ID = None
    ID_Aqcuired = False
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

print(get_ID())


serialcomm.close()
