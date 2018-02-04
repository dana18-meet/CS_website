from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
 
@app.route('/')
def index():
	return render_template("home.html")

@app.route('/gapyear')
def one():
	return render_template("gap_year.html")

@app.route('/boardingschool')
def two():
	return render_template("boarding_school.html")

@app.route('/summerprograms')
def three():
	return render_template("summer_programs.html")

@app.route('/summercamps')
def four():
    return render_template("summer_camps.html")
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

# class stuff(db.Model):
#     __tablename__ = "stuff"
#     color = db.Column('#FFC300', db.Unicode)
#         weight = db.Column('300', db.Integer)

#  db.create_all()

 # @app.route('/submit_form', methods=['POST'])
 # def submit_form():
 # 	<form action="{{ url_for('submit_form') }}" method="post">

  




if __name__ == "__main__":
	app.run()

