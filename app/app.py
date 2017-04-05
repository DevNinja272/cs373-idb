from flask import Flask, render_template, json, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
from models import State, University, Degree, DegreesUniversities
from config import db_config
import subprocess
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://" + db_config['user'] + ":" + db_config['pass'] + "@" + db_config['host'] + "/" + db_config['db_name']
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Session = sessionmaker(bind = engine)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/api/universities/<int:id>',methods=['GET'])
def get_single_uni(id):
  session = Session()
  uni = session.query(University).get(id)
  state = session.query(State).filter(State.id == uni.state_id).one()
  uni.state_name = str(state.name)
  uni.state_id = state.id

  degreesUniversitiesList = session.query(DegreesUniversities).filter(DegreesUniversities.university_id == uni.id).all()
  degree_list = []
  for degreeUniversity in degreesUniversitiesList:
    degree = session.query(Degree).get(degreeUniversity.degree_id)
    degree_dict = {"degree_id":degree.id, "degree_name":str(degree.name)}
    degree_list.append(degree_dict)

  uni_dict = uni.__dict__.copy()
  uni_dict['degrees'] = degree_list
  uni_dict.pop('_sa_instance_state', None)
  return jsonify(university=uni_dict)


@app.route('/api/degrees/<int:id>',methods=['GET'])
def get_single_degree(id):
  session = Session()
  degree = session.query(Degree).get(id)

  degreesUniversitiesList = session.query(DegreesUniversities).filter(DegreesUniversities.degree_id == degree.id).all()
  universities_list = []
  for degreeUniversity in degreesUniversitiesList:
    university = session.query(University).get(degreeUniversity.university_id)
    university_dict = {"university_id":university.id, "university_name": str(university.name)}
    universities_list.append(university_dict)

  degree_dict = degree.__dict__.copy()
  degree_dict['universities'] = universities_list
  degree_dict.pop('_sa_instance_state', None)
  return jsonify(degree=degree_dict)



@app.route('/api/states/<int:id>',methods=['GET'])
def get_single_state(id):
    session = Session()
    state = session.query(State).get(id)

    universities_row_list = session.query(University).join(State).filter(State.id == state.id).all()
    universities_list = []
    for row in universities_row_list:
        university_dict = {"university_id":row.id, "unviersity_name":str(row.name)}
        universities_list.append(university_dict)

    state_dict = state.__dict__.copy()
    state_dict['universities'] = universities_list
    state_dict.pop('_sa_instance_state', None)
    return jsonify(state=state_dict)


@app.route('/api/universities',methods=['GET'])
def get_unis():
  session = Session()
  universities = []
  for uni in session.query(University).all():
    uni_dict = uni.__dict__.copy()
    uni_dict.pop('_sa_instance_state', None)
    universities.append(uni_dict)
  return jsonify(universities=universities)

@app.route('/api/states',methods=['GET'])
def get_states():
  session = Session()
  states = []
  for state in session.query(State).all():  
    state_dict = state.__dict__.copy()
    state_dict.pop('_sa_instance_state', None)
    states.append(state_dict)

  return jsonify(states=states)

@app.route('/api/degrees',methods=['GET'])
def get_degrees():
  session = Session()
  degrees = []
  for degree in session.query(Degree).all():
    degree_dict = degree.__dict__.copy()
    degree_dict.pop('_sa_instance_state', None)
    degrees.append(degree_dict)

  return jsonify(degrees=degrees)

@app.route('/runtests',methods=['GET'])
def runtests():
  try:
    proc = subprocess.check_output(["python","tests.py"], stderr= subprocess.STDOUT, universal_newlines=True)
  except subprocess.CalledProcessError as e:
    print(e.output)
    proc = 'error. Check console'
  return str(proc) 


if __name__ == "__main__":
    app.run(debug=True)