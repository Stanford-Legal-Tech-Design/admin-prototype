from flask import Flask, render_template
 
app = Flask(__name__)      
 
@app.route('/')
def home():
  return render_template('home.html')

@app.route('/status')
def about():
	if user_choice == "released":
		return render_template("released.html", choice = user_choice)
	else:
		return render_template("held.html", choice = user_choice)

@app.route('/nextsteps')
def about():
	return
	
if __name__ == '__main__':
  app.run(debug=True)