from flask import Flask, render_template
 
app = Flask(__name__)      
 
@app.route('/')
def home():
  return render_template('home.html')

@app.route('/start')
def start():
	action = request.args.get("start")
	if action == "schedule":
		return render_template("type.html")
	else:
		return render_template("modify.html")

@app.route('/message')
def type():
	person = request.form.get("type")
	if person == "juvenile":
		return render_template("juvenile.html")
	else:
		return render_template("adult.html")

@app.route('/status')
def about():
	action = request.args.get("statuschoice")
	if user_choice == "released":
		return render_template("released.html", choice = user_choice)
	else:
		return render_template("held.html", choice = user_choice)
 
if __name__ == '__main__':
  app.run(debug=True)