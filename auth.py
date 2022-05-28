#Imports
import firebase_admin
import pyrebase
import json
from firebase_admin import credentials, auth
from flask import Flask, request
#App configuration
app = Flask(__name__)
#Connect to firebase
cred = credentials.Certificate('fb-credentials.json')
firebase = firebase_admin.initialize_app(cred)
pb = pyrebase.initialize_app(json.load(open('fbconfig.json')))
#Data source
users = [{'uid': 1, 'name': 'Noah Schairer'}]
#Api route to get users
@app.route('/api/userinfo')
def userinfo():
    return {'data': users}, 200

#Api route to sign up a new user
@app.route('/api/signup') 
def signin(): #Signs into the system
    #email = request.form.get('email')
    #password = request.form.get('password')
    if phone is None or len(phone) != 10:
        return {'message': 'Invalid Phone Number'},400
    try:
        user = auth.create_user(
               phone=phone
        )
        return {'message': f'Successfully created user {user.uid}'},200
    except:
        return {'message': 'Error creating user'},400

#Api route to get a new token for a valid user
@app.route('/api/token')
def token():
    phone = request.form.get('phone')
    try:
        user = pb.auth().sign_in_with_email_and_password(phone)
        jwt = user['idToken']
        return {'token': jwt}, 200
    except:
        return {'message': 'There was an error logging in'},400
if __name__ == '__main__':
    app.run(debug=True)