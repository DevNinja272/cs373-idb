import subprocess
import os
import requests
from urllib.request import urlopen

from flask import Flask, render_template, json, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine, func, Table, Column, Float, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from models import State, University, Degree, DegreesUniversities
from models import db
 
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://master:Test123alloc@allocpg.cbdyaoty0djb.us-west-2.rds.amazonaws.com/collegedb'
# engine = create_engine('postgresql://master:Test123alloc@allocpg.cbdyaoty0djb.us-west-2.rds.amazonaws.com/collegedb')
# Session = sessionmaker(bind = engine)

def import_data(url):
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
  degrees = {
    '2014.academics.program_percentage.agriculture': 'Agriculture, Agriculture Operations, and Related Sciences',
    '2014.academics.program_percentage.resources': 'Natural Resources and Conservation',
    '2014.academics.program_percentage.architecture': 'Architecture and Related Services',
    '2014.academics.program_percentage.ethnic_cultural_gender': 'Area, Ethnic, Cultural, Gender, and Group Studies'
  }
  degree_models = {}
  degree_private_counts = {}
  degree_public_counts = {}

  response = urlopen(url)
  json_response = json.load(response)
  print('Number of Pages:' + str(json_response["metadata"]["total"]))
  print('Current Page:' + str(json_response["metadata"]["page"]))
  print('Results per page:' + str(json_response["metadata"]["per_page"]))

  for region in regions:
    for st in region["states"]:
      state = State()
      state.name = st
      state.region = region["name"]
      state.average_public_cost = 0
      state.average_private_cost = 0
      state.number_colleges = 0

      state.num_public = 0
      state.num_private = 0

      states.append(state)

  for i in json_response["results"]:

    state_name = i["school.state"]
    state = next(state for state in states if state.name == state_name)

    if i["2014.cost.attendance.academic_year"] is None:
      cost = 0
    else:
      cost = i["2014.cost.attendance.academic_year"] 

    if i["school.ownership"] == 1:
      state.num_public = state.num_public + 1
      state.average_public_cost = state.average_public_cost + cost
    else:
      state.num_private = state.num_private + 1
      state.average_private_cost = state.average_private_cost + cost

  for i in states:
    i.number_colleges = i.num_public + i.num_private
    if (i.num_public == 0):
      i.average_public_cost = 0
    else:
      i.average_public_cost = i.average_public_cost // i.num_public

    if (i.num_private == 0):
      i.average_private_cost = 0
    else:
      i.average_private_cost = i.average_private_cost // i.num_private

  for i in states:
    db.session.add(i)

  db.session.commit()

  for degree_code, degree_name in degrees.items():
    degree = Degree()
    degree.name = degree_name
    degree.num_public_offer = 0
    degree.num_private_offer = 0
    degree.num_percent_public = 0
    degree.num_percent_private = 0
    degree_models[degree_code] = degree
    degree_private_counts[degree_code] = 0
    degree_public_counts[degree_code] = 0

  for i in json_response["results"]:

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

    # Add available degrees
    for degree_code in degrees:
      if i[degree_code] > 0:
        association = DegreesUniversities()
        association.degree = degree_models[degree_code]
        uni.degrees.append(association)
        db.session.add(association)
        if uni.is_public:
          degree_public_counts[degree_code] += 1
        else:
          degree_private_counts[degree_code] += 1

    db.session.add(uni)

  for degree_code, degree in degree_models.items():
    total = degree_public_counts[degree_code] + degree_private_counts[degree_code]
    degree.num_public_offer = degree_public_counts[degree_code]
    degree.num_private_offer = degree_private_counts[degree_code]
    degree.num_percent_public = degree_public_counts[degree_code]/total
    degree.num_percent_private = degree_private_counts[degree_code]/total
    db.session.add(degree)

  db.session.commit()

  return json_response["metadata"]["total"]

if __name__ == "__main__":
  db.create_all()

  # Add in the state constraint or other constraints to just import a subset of the data.
  url_first_part = 'https://api.data.gov/ed/collegescorecard/v1/schools.json?page='
  url_second_part = '&school.degrees_awarded.highest=4&school.ownership=1,2&school.degrees_awarded.predominant=3&per_page=70&_fields=school.state,school.name,school.school_url,school.ownership,2014.cost.attendance.academic_year,2014.student.size,\
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
&api_key=oWaDjGHFWwjaQLhN7BUTyYYFUGBONKxo07ZU2E0W'
  
  page = 0
  while import_data(url_first_part + str(page) + url_second_part) > page:
    page += 1
  print("Completed import.")
