from twilio.rest import Client

SID = ""
TOKEN = ""

client = Client(SID, TOKEN)

message = client.messages.create(
    to = "", #Write number here
    from_ = "", #Insert Twilio number
    body = "Hello World!"
)

print(message.sid)

#Function to notify user their luggage is on the conveyer belt
def cNotif(phoneNo, lName): #Phone number, luggage name/identifier
    #if lname status is equal to conveyor belt value, then send the notification, otherwise do nothing
    pass

#Function to confirm to users their luggage has been picked up
def pNotif(phoneNo, lName): #Phone number, luggage name/identifier
    #if lname status is picked up, then send notification, otherwise do nothing
    pass