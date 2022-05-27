from twilio.rest import Client

SID = ""
TOKEN = ""

client = Client(SID, TOKEN)

#print(message.sid)

#Function to notify user their luggage is on the conveyer belt
def cNotif(phoneNo, luggageID): #Phone number, luggageID
    content = "Your luggage with ID " + luggageID + " is on the conveyor belt and ready for pickup"
    message = client.messages.create(
        to = phoneNo, #Write number here
        from_ = "", #Insert Twilio number
        body = content
    )
    return

#Function to confirm to users all their luggage has been picked up
def pNotif(phoneNo): #Phone number, luggage name/identifier
    message = client.messages.create(
        to = phoneNo, #Write number here
        from_ = "", #Insert Twilio number
        body = "Your luggage has been picked up"
    )
    return