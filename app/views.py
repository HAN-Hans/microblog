# The views are the handlers that respond to requests 
# from web browsers or other clients. In Flask handlers 
# are written as Python functions. Each view function 
# is mapped to one or more request URLs.


from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname':'Justin'}	# fake user
	posts = [
	{
		'author':{'nickname':'John'},
		'body':'Beautiful day in Portland!'
	},
	{
		'author':{'nickname':'Susan'},
		'body':'The Avengers movie was so cool!'
	}]
	return render_template('index.html',
		title = 'Home',
		user = user,
		posts = posts)
