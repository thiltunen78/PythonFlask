from app import app
#render_template gives you access to Jinja2 template engine
from flask import render_template,request,make_response,flash,redirect
from app.forms import LoginForm
from app.forms import RegisterForm
from app.db_models import Users
from app import db

@app.route('/',methods=['GET','POST'])
def index():
	login = LoginForm()
	#check if get method
	if request.method == 'GET':
		return render_template('template_index.html',form=login)
	else:
		#check if form data is valid
		if login.validate_on_submit():
			print(login.email.data)
			print(login.passw.data)
			return render_template('template_user.html')
		#form data was not valid
		else:
			flash('Give proper information to email ad password fields')
			return render_template('template_index.html',form=login)

@app.route('/register',methods=['GET','POST'])
def registerUser():
	register = RegisterForm()
	#check if get method
	if request.method == 'GET':
		return render_template('template_register.html',form=register)
	else:
		#check if form data is valid
		if register.validate_on_submit():
			user = Users(register.email.data,register.passw.data)
			db.session.add(user)
			db.session.commit()
			flash("Name {0} registered".format(register.email.data))
			return redirect('/')
		#form data was not valid
		else:
			flash('invalid email or no password given')
			return render_template('template_register.html',form=register)

		
@app.route('/user/<name>')
def user(name):
	print(request.headers.get('User-Agent'))
	return render_template('template_user.html',name=name)

#Example how you can define route methods
@app.route('/user',methods=['GET','POST'])
def userParams():
	name = request.args.get('name')
	return render_template('template_user.html',name=name)

#this is comment also, but you can use only one line
"""This is comment
   you can use multiple lines"""