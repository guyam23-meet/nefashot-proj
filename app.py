from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase


Config = {
  "apiKey": "AIzaSyBSI-iNkNgm0yHq-EHFOq7LpKmL3rdOMrE",
  "authDomain": "nefashot-proj.firebaseapp.com",
  "projectId": "nefashot-proj",
  "storageBucket": "nefashot-proj.appspot.com",
  "messagingSenderId": "1083253811116",
 "appId": "1:1083253811116:web:68d77ae866b32a2b767c09",
  "measurementId": "G-8R4V5S49XD",
  "databaseURL":"https://nefashot-proj-default-rtdb.europe-west1.firebasedatabase.app/"
}


firebase= pyrebase.initialize_app(Config)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


#start coding




#end coding

if __name__ == '__main__':
  app.run(debug=True)