from app import app
#render_template gives you access to Jinja2 template engine
from flask import render_template,request,make_response,flash,redirect,session
from app.forms import LoginForm,RegisterForm,FriendForm
from app.db_models import Users
from app import db

#for sql error handling 


@app.route('/',methods=['GET','POST'])
def index():
	login = LoginForm()
	#Check if get method
	if request.method == 'GET':
		return render_template('template_index.html',form=login)
	else:
		#check if form data is valid
		if login.validate_on_submit():
			#Check id correct useranme and password
			user = Users.query.filter_by(email=login.email.data).filter_by(passw=login.passw.data)
			print(user)
			if user.count() == 1:
				print(user[0])
				session['user_id'] = user[0].id
				print(session['user_id'])
				return render_template('template_user.html')
			else:
				flash('Wrong email or password')
				return render_template('template_index.html',form=login)
		#form data was not valid
		else:
			flash('Give proper information to email and password fields!')
			return render_template('template_index.html',form=login)

@app.route('/register',methods=['GET','POST'])
def registerUser():
	form = RegisterForm()
	if request.method == 'GET':
		return render_template('template_register.html',form=form)
	else:
		if form.validate_on_submit():
			user = Users(form.email.data,form.passw.data)
			try:
				db.session.add(user)
				db.session.commit()
			except:
				db.session.rollback()
				flash('Username allready in use')
				return render_template('template_register.html',form=form)
			flash("Name {0} registered.".format(form.email.data))
			return redirect('/')
		else:
			flash('Invalid email address or no password given')
			return render_template('template_register.html',form=form)
		

@app.route('/friends',methods=['GET','POST'])
def friends():
	form = FriendForm()
	if request.method == 'GET':
		return render_template('template_friends.html',form=form)
	
		
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