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
	if not ('admin' in login_session):
		login_session['admin']=False
	return render_template('about.html')


@app.route('/blog', methods=['GET', 'POST'])
def blog():
	if not ('admin' in login_session):
		login_session['admin'] = False
	if request.method == 'POST':
		if request.form['msg'] != "":
			message = {"msg" : request.form['msg']}
			db.child('Messages').push(message)
			return render_template('blog.html', message = db.child('Messages').get().val(),admin=login_session['admin'])
	return render_template('blog.html', message = db.child('Messages').get().val(),admin=login_session['admin'])

@app.route('/admin',methods=['POST','GET'])
def admin():
	failed_password=False
	login_session['admin']=False
	password="123"
	if request.method=='POST':
		if request.form['password']==password:
			login_session['admin']=True
		else:
			failed_password=True
	return render_template('admin.html',admin=login_session['admin'],failed_password=failed_password)

@app.route('/remove/<string:i>', methods=['GET', 'POST'])
def remove(i):
	db.child('Messages').child(i).remove()
	return redirect(url_for('blog'))




@app.route('/contact',methods=['POST','GET'])
def contact():
	return render_template('contact.html',schedule=db.child('schedule').get().val(),periods=db.child('periods').get().val())

@app.route('/volunteer', methods=['POST', 'GET'])
def volunteer():
	if request.method == 'POST':
		name = request.form['full_name']
		street = request.form['street']
		zipcode = request.form['zip']
		phone = request.form['phone']
		email = request.form['your_email']
		info = {"name": name, "street": street, "zipcode": zipcode, "phone": phone}
		db.child("Volunteers").push(info)
		return render_template('info.html', volunteers = db.child("Volunteers").get().val())
	return render_template('info.html', volunteers = db.child("Volunteers").get().val())

@app.route('/schedule')
def schedule():
	return render_template('schedule.html')
#end coding


if __name__ == '__main__':
	app.run(debug=True)
