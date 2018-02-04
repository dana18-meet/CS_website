from flask import Flask, Response, render_template, request, redirect
# SQLAlchemy
from sqlalchemy import create_engine, Column, DateTime, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
engine = create_engine('sqlite:///project.db')
db.metadata.bind = engine
DBSession = sessionmaker (bind=engine)
session = DBSession ()

db.create_all()
 
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

# class stuff(db.Model):
#     __tablename__ = "stuff"
#     color = db.Column('#FFC300', db.Unicode)
#         weight = db.Column('300', db.Integer)

#  db.create_all()

 # @app.route('/submit_form', methods=['POST'])
 # def submit_form():
 # 	<form action="{{ url_for('submit_form') }}" method="post">

  




#if __name__ == "__main__":
#	app.run()

