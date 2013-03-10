from flask import Flask,render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flask_db'
db = SQLAlchemy(app)



##########################

##########################
# Controller
##########################
@app.route("/")
def index():
	return render_template('index.html')

@app.route('/home')
def home():
	return render_template('main.html')

if __name__ == '__main__':
	app.run()