from flask import Flask, render_template, request, url_for, redirect
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/', methods =['GET', 'POST']) 
def home():  
	if request.method == 'POST':
		login_session['quote'] = request.form['info']
		login_session["quote's author"] = request.form['info1']
		login_session['age'] = request.form['info2']
		return render_template('thanks.html') 
	
	else : 
		return render_template('home.html')





@app.route('/error')
def error():

	return render_template('error.html')


@app.route('/display')
def display():

	return render_template('display.html',login_session=login_session ) 


@app.route('/thanks')
def thanks():

	return render_template('thanks.html')


if __name__ == '__main__':
	app.run(debug=True)