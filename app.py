from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase


config = {
	"apiKey": "AIzaSyBSI-iNkNgm0yHq-EHFOq7LpKmL3rdOMrE",
	"authDomain": "nefashot-proj.firebaseapp.com",
	"projectId": "nefashot-proj",
	"storageBucket": "nefashot-proj.appspot.com",
	"messagingSenderId": "1083253811116",
 "appId": "1:1083253811116:web:68d77ae866b32a2b767c09",
	"measurementId": "G-8R4V5S49XD",
	"databaseURL":"https://nefashot-proj-default-rtdb.europe-west1.firebasedatabase.app/"
}


firebase= pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


#start coding

@app.route('/', methods=['GET', 'POST'])
def home():
	login_session['admin']=False
  return render_template('about.html')


@app.route('/blog', methods=['GET', 'POST'])
def blog():
	if 'admin' not in login_session:
		login_session['admin'] = False
	if request.method == 'POST':
		if request.form['msg'] != "":
			message = {"msg" : request.form['msg']}
			db.child('Messages').push(message)
			return render_template('blog.html', message = db.child('Messages').get().val(),admin=login_session['admin'])
	return render_template('blog.html', message = db.child('Messages').get().val(),admin=login_session['admin'])

@app.route('/admin',methods=['POST','GET'])
def admin():
	login_session['admin']=False
	password="123"
	if request.method=='POST':
		if request.form['password']==password:
			login_session['admin']=True
	return render_template('admin.html',admin=login_session['admin'])

@app.route('/remove', methods=['GET', 'POST'])
def remove(i):
	db.child('Messages').child(i).remove()
	return redirect(url_for('blog'))

#end coding


if __name__ == '__main__':
	app.run(debug=True)
