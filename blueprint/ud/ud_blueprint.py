from flask import Blueprint,session,redirect

#create blueprint
#first argument is the name of the blueprint folder
#second is always __name__ attribute
#third parameter tells what folder contains your templates
ud = Blueprint('ud',__name__,template_folder='templates',url_prefix=('/app/'))

#/app/delete
@ud.route('delete/<int:id>')
def delete(id):
	return "delete"

@ud.route('update')
def update():
	return "update"

def before_request():
	if not 'isLogged' in session:
		return redirect('/')
	
ud.before_request(before_request)