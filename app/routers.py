from app import app

#render_template gives you access to jinja2 template engine
from flask import render_template,request,make_response

@app.route('/')
def index():
	name = 'tero'
	address = 'tie3'
	return render_template('template_index.html',title=address,name=name)

@app.route('/index')
def index2():
	response = make_response(render_template('template_index.html',title='otsikko',name='nimi')) 
	response.headers.add('Cache-Control','no-cache') 
	return response

@app.route('/user/<name>')
def user(name):
	print(request.headers.get('User-Agent'))
	return render_template('template_user.html',name=name)

#example how you can define route methods
@app.route('/user',methods=['GET','POST'])
def userParams():
	name=request.args.get('name')
	return render_template('template_user.html',name=name)