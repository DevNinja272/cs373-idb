from flask import Flask, render_template, json, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
from model import State, University, Degree, DegreesUniversities

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://master:Test123alloc@allocpg.cbdyaoty0djb.us-west-2.rds.amazonaws.com/collegedb'
engine = create_engine('postgresql://master:Test123alloc@allocpg.cbdyaoty0djb.us-west-2.rds.amazonaws.com/collegedb')
Session = sessionmaker(bind = engine)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/universities',methods=['GET'])
def get_unis():
  session = Session()
  universities = []
  for uni in session.query(University).all():
    state = session.query(State).filter(State.id == uni.state_id).one()
    uni.state_name = str(state.name)
    uni.state_id = state.id

    degrees = session.query(DegreesUniversities).filter(DegreesUniversities.university_id == uni.id).all()
    list_degree_ids = []
    for degree in degrees:
      list_degree_ids.append(degree.degree_id)
    print(list_degree_ids)

    uni_dict = uni.__dict__.copy()
    uni_dict['degrees'] = list_degree_ids
    uni_dict.pop('_sa_instance_state', None)
    universities.append(uni_dict)
  return jsonify(universities=universities)

@app.route('/states',methods=['GET'])
def get_states():
  session = Session()
  states = []
  for state in session.query(State).all():

    state.unis = []
    for uni in session.query(University).all():
      if str(uni.state_id) == str(state.id):
        uni_dict = uni.__dict__.copy()
        uni_dict.pop('_sa_instance_state', None)
        state.unis.append(uni_dict)


    state_dict = state.__dict__.copy()
    state_dict.pop('_sa_instance_state', None)
    states.append(state_dict)

  return jsonify(states=states)

@app.route('/degrees',methods=['GET'])
def get_degrees():
  session = Session()
  degrees = []
  for degree in session.query(Degree).all():
    universities = session.query(DegreesUniversities).filter(DegreesUniversities.degree_id == degree.id).all()
    list_university_ids = []
    for university in universities:
      list_university_ids.append(university.university_id)

    degree_dict = degree.__dict__.copy()
    degree_dict['universities'] = list_university_ids
    degree_dict.pop('_sa_instance_state', None)
    degrees.append(degree_dict)

  return jsonify(degrees=degrees)

if __name__ == "__main__":
    app.run()