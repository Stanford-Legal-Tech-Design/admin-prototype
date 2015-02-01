from flask import Flask, render_template, request
 
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

@app.route('/status')
def type():
	person = request.args.get("type")
	if person == "juvenile":
		return render_template("juvenilestatus.html")
	else:
		return render_template("adultstatus.html")

@app.route('/nextsteps')
def status():
	status = request.args.get("statuschoice")
	if status == "released":
		return render_template("released.html")
	else:
		return render_template("held.html")
 
@app.route('/text-options', methods=['GET', 'POST'])
def options():
	jname = request.form.get("jname")
	pname = request.form.get("pname")
	jnumber = request.form.get("jnumber")
	pnumber = request.form.get("pnumber")
	return render_template("messaging.html", jname = jname, pname = pname, jnumber = jnumber)

if __name__ == '__main__':
  app.run(debug=True)


