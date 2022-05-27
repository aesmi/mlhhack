from twilio.rest import Client
import datetime
import json

file = open("twilio-info.json")
data = json.load(file)

SID = data["SID"]
TOKEN = data["TOKEN"]
twilioNum = data["Phone-no"]

client = Client(SID, TOKEN)

#Function to notify user their luggage is on the conveyer belt
def cNotif(phoneNo, luggageID, statNo): #Phone number, luggage ID, Station number
    content = "Your luggage with ID " + luggageID + " is ready for pickup at " + statNo
    message = client.messages.create(
        to = phoneNo, #Write number here
        from_ = twilioNum, #Insert Twilio number
        body = content
    )
    return


#Function to confirm to users all their luggage has been picked up
def pNotif(phoneNo, statNo): #Phone number, Station number
    now = datetime.datetime.now()
    tInfo = now.strftime("%b-%d-%Y %H:%M:%S")   

    message = client.messages.create(
        to = phoneNo, #Write number here
        from_ = twilioNum, #Insert Twilio number
        body = "Your luggage has been picked up from " + statNo + " at " + tInfo
    )
    return