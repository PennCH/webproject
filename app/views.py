from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
	user = { 'nickname': 'Rocky' }
	posts = [
		{
			'author':{'authorname':'文浩'},
			'body':'Beautiful day in ShiJiaZhuang'
		},
		{
			'author':{'authorname':'允涵'},
			'body':'Beautiful day in LuanCheng'
		}
	]
	return render_template("index.html",
							title = 'Home',
							user = user,
						   	posts = posts)