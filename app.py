from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config = {
  "apiKey": "AIzaSyC2DHVKTK5dauvHhzqhsm8FVLrQqbtNc30",
  "authDomain": "the-project-3a481.firebaseapp.com",
  "projectId": "the-project-3a481",
  "storageBucket": "the-project-3a481.appspot.com",
  "messagingSenderId": "382041353587",
  "appId": "1:382041353587:web:de4243a1bae8b43738e906",
  "measurementId": "G-FPJ1G3R55F",
  "databaseURL":"https://the-project-3a481-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase=pyrebase.initialize_app(config)
auth=firebase.auth()
db = firebase.database()

@app.route('/volunteer', methods=['GET', 'POST'])
def signup():
   error = ""
   if request.method == 'POST':
       name = request.form['name']
       number = request.form['number']
       living = request.form['living']
       reason = request.form['reason']
       age = request.form['age']
       mail = request.form['mail']
       lang = request.form['lang']
       try:
       	login_session['user'] = 
auth.create_user_with_name_and_number_and_living_and_reason_and_age_and_mail_and_lang(name,number,living,reason,age,mail,lang)
           return redirect(url_for('home'))
       except:
           error = "Authentication failed"
   return render_template("volunteer.html")
