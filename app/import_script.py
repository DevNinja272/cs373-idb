import subprocess
import os
import requests
from urllib.request import urlopen

from flask import Flask, render_template, json, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine, func, Table, Column, Float, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model import State, University
from model import db
 
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://master:Test123alloc@allocpg.cbdyaoty0djb.us-west-2.rds.amazonaws.com/collegedb'
# engine = create_engine('postgresql://master:Test123alloc@allocpg.cbdyaoty0djb.us-west-2.rds.amazonaws.com/collegedb')
# Session = sessionmaker(bind = engine)

if __name__ == "__main__":
  db.create_all()
  universities = []
  states = []
  regions =   [ 
          {"name": "New England", "states": ('CT', 'ME', 'MA', 'NH', 'RI', 'VT')},
          {"name": "Mentry_id East", "states": ('DE', 'DC', 'MD', 'NJ', 'NY', 'PA')},
          {"name": "Great Lakes", "states": ('IL', 'IN', 'MI', 'OH', 'WI')},
          {"name": "Plains", "states": ('IA', 'KS', 'MN', 'MO', 'NE', 'ND', 'SD')},
          {"name": "Southeast", "states": ('AL', 'AR', 'FL', 'GA', 'KY', 'LA', 'MS', 'NC', 'SC', 'TN', 'VA', 'WV')},
          {"name": "Southwest", "states": ('AZ', 'NM', 'OK', 'TX')},
          {"name": "Rocky Mountains", "states": ('CO', 'entry_id', 'MT', 'UT', 'WY')},
          {"name": "Far West", "states": ('AK', 'CA', 'HI', 'NV', 'OR', 'WA')},
          {"name": "Outlying Areas", "states": ('AS', 'FM', 'GU', 'MH', 'MP', 'PR', 'PW', 'VI')},
        ]
  degrees = [
    {'2014.academics.program_percentage.agriculture': 'Agriculture, Agriculture Operations, and Related Sciences'},
    {'2014.academics.program_percentage.resources': 'Natural Resources and Conservation'}
  ]

  url = "https://api.data.gov/ed/collegescorecard/v1/schools.json?school.state=TX,FL&school.degrees_awarded.highest=4&school.ownership=1,2&school.degrees_awarded.predominant=3&per_page=70&_fields=school.state,school.name,school.school_url,school.ownership,2014.cost.attendance.academic_year,2014.student.size\
2014.academics.program_percentage.agriculture,\
2014.academics.program_percentage.resources,\
2014.academics.program_percentage.architecture,\
2014.academics.program_percentage.ethnic_cultural_gender,\
2014.academics.program_percentage.communication,\
2014.academics.program_percentage.communications_technology,\
2014.academics.program_percentage.computer,\
2014.academics.program_percentage.personal_culinary,\
2014.academics.program_percentage.education,\
2014.academics.program_percentage.engineering,\
2014.academics.program_percentage.engineering_technology,\
2014.academics.program_percentage.language,\
2014.academics.program_percentage.family_consumer_science,\
2014.academics.program_percentage.legal,\
2014.academics.program_percentage.english,\
2014.academics.program_percentage.humanities,\
2014.academics.program_percentage.library,\
2014.academics.program_percentage.biological,\
2014.academics.program_percentage.mathematics,\
2014.academics.program_percentage.military,\
2014.academics.program_percentage.multidiscipline,\
2014.academics.program_percentage.parks_recreation_fitness,\
2014.academics.program_percentage.philosophy_religious,\
2014.academics.program_percentage.theology_religious_vocation,\
2014.academics.program_percentage.physical_science,\
2014.academics.program_percentage.science_technology,\
2014.academics.program_percentage.psychology,\
2014.academics.program_percentage.security_law_enforcement,\
2014.academics.program_percentage.public_administration_social_service,\
2014.academics.program_percentage.social_science,\
2014.academics.program_percentage.construction,\
2014.academics.program_percentage.mechanic_repair_technology,\
2014.academics.program_percentage.precision_production,\
2014.academics.program_percentage.transportation,\
2014.academics.program_percentage.visual_performing,\
2014.academics.program_percentage.health,\
2014.academics.program_percentage.business_marketing,\
2014.academics.program_percentage.history,\
&api_key=oWaDjGHFWwjaQLhN7BUTyYYFUGBONKxo07ZU2E0W"

  response = urlopen(url)
  json = json.load(response)

  for region in regions:
    for st in region["states"]:
      state = State()
      state.name = st
      state.region = region["name"]
      state.average_public_cost = 0
      state.average_private_cost = 0
      state.number_colleges = 0

      state.numPublic = 0
      state.numPrivate = 0

      states.append(state)

  for i in json["results"]:

    state_name = i["school.state"]
    state = next(state for state in states if state.name == state_name)

    if i["2014.cost.attendance.academic_year"] is None:
      cost = 0
    else:
      cost = i["2014.cost.attendance.academic_year"] 

    if i["school.ownership"] == 1:
      state.numPublic = state.numPublic + 1
      state.average_public_cost = state.average_public_cost + cost
    else:
      state.numPrivate = state.numPrivate + 1
      state.average_private_cost = state.average_private_cost + cost

  for i in states:
    i.number_colleges = i.numPublic + i.numPrivate
    if (i.numPublic == 0):
      i.average_public_cost = 0
    else:
      i.average_public_cost = i.average_public_cost // i.numPublic

    if (i.numPrivate == 0):
      i.average_private_cost = 0
    else:
      i.average_private_cost = i.average_private_cost // i.numPrivate

  for i in states:
    db.session.add(i)

  db.session.commit()

  for i in json["results"]:

    uni = University()
    uni.name = i["school.name"]
    if i["school.ownership"] == 1:
      uni.is_public = True
    else:
      uni.is_public = False

    uni.website_URL = str(i["school.school_url"])
    uni.academic_cost = i["2014.cost.attendance.academic_year"]
    uni.num_students = i["2014.student.size"]
    
    state_name = i["school.state"]
    state = next(state for state in states if state.name == state_name)
    uni.state_id = state.id
    db.session.add(uni)

  db.session.commit()