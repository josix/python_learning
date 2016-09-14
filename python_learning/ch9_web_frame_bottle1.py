from bottle import route, run

@route('/') # the home page('/'), is home() deal with
def home():
	return "It isn't fancy, but it it's my home page"

run(host = 'localhost', port = 9999)