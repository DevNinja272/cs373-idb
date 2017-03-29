from flask import Flask, render_template, json, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
from model import State, University

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
    uni.state_entry_id = state.entry_id

    uni_dict = uni.__dict__.copy()
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

if __name__ == "__main__":
    app.run()