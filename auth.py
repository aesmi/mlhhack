# Imports
import firebase_admin
import json
from firebase_admin import credentials, auth
from flask import Flask, request

# App configuration
app = Flask(__name__)
# Connect to firebase
# https://firebase.google.com/docs/admin/setup#python
cred = credentials.Certificate("fb-credentials.json")
firebase = firebase_admin.initialize_app(cred)

# Data source
users = [{"uid": 1, "name": "random"}]
# Api route to get users
@app.route("/api/")
def userinfo():
    return {"data": users}, 200


# Api route to sign up a new user
@app.route("/api/signin")
def signin():  # Signs into the system
    phone = request.form.get("phone")
    # makes sure phone exists and is of appropriate length (we could handle this however on the frontend with form validation)
    if phone is None or len(phone) != 10:
        return {"message": "Invalid Phone Number"}, 400
    try:
        user = auth.create_user(phone=phone)
        return {"message": f"Successfully created user {user.uid}"}, 200
    except:
        return {"message": "Error creating user"}, 400


# Api route to get a new token for a valid user
@app.route("/api/token")
def token():
    phone = request.form.get("phone")
    try:
        # get user
        user = auth.get_user(phone)
        # get token
        token = auth.create_custom_token(user.uid)
        return {"token": token}, 200
    except:
        return {"message": "There was an error logging in"}, 400


if __name__ == "__main__":
    app.run(debug=True)
