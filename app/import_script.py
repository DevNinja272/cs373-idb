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
from math import floor

from config import db_config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://" + db_config['user'] + ":" + db_config['pass'] + "@" + db_config['host'] + "/" + db_config['db_name']
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Session = sessionmaker(bind = engine)

def floored_percentage(val, digits):
    val *= 10 ** (digits + 2)
    return '{1:.{0}f}'.format(digits, floor(val) / 10 ** digits)

if __name__ == "__main__":
  db.create_all()
  universities = []
  states = []

  states_abbrevs = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

  regions =   [ 
          {"name": "New England", "states": ('CT', 'ME', 'MA', 'NH', 'RI', 'VT')},
          {"name": "Mentry_id East", "states": ('DE', 'DC', 'MD', 'NJ', 'NY', 'PA')},
          {"name": "Great Lakes", "states": ('IL', 'IN', 'MI', 'OH', 'WI')},
          {"name": "Plains", "states": ('IA', 'KS', 'MN', 'MO', 'NE', 'ND', 'SD')},
          {"name": "Southeast", "states": ('AL', 'AR', 'FL', 'GA', 'KY', 'LA', 'MS', 'NC', 'SC', 'TN', 'VA', 'WV')},
          {"name": "Southwest", "states": ('AZ', 'NM', 'OK', 'TX')},
          {"name": "Rocky Mountains", "states": ('CO', 'ID', 'MT', 'UT', 'WY')}, 
          {"name": "Far West", "states": ('AK', 'CA', 'HI', 'NV', 'OR', 'WA')},
          {"name": "Outlying Areas", "states": ('GU', 'PR','VI')},
        ]
  degrees = {
    '2014.academics.program_percentage.agriculture': 'Agriculture, Agriculture Operations, and Related Sciences',
    '2014.academics.program_percentage.resources': 'Natural Resources and Conservation',
    '2014.academics.program_percentage.architecture': 'Architecture and Related Services',
    '2014.academics.program_percentage.ethnic_cultural_gender': 'Area, Ethnic, Cultural, Gender, and Group Studies',
    '2014.academics.program_percentage.communication': 'Communication, Journalism, And Related Programs',
    '2014.academics.program_percentage.communications_technology':'Communications Technologies/Technicians And Support Services',
    '2014.academics.program_percentage.computer':'Computer And Information Sciences And Support Services',
    '2014.academics.program_percentage.personal_culinary':'Personal And Culinary Service',
    '2014.academics.program_percentage.education': 'Education',
    '2014.academics.program_percentage.engineering': 'Engineering',
    '2014.academics.program_percentage.engineering_technology': 'Engineering Technologies And Engineering-Related Fields',
    '2014.academics.program_percentage.language': 'Foreign Languages, Literatures, And Linguistic',
    '2014.academics.program_percentage.family_consumer_science': 'Family And Consumer Sciences/Human Sciences',
    '2014.academics.program_percentage.legal':'Legal Professions And Studies',
    '2014.academics.program_percentage.english': 'English Language And Literature/Letters',
    '2014.academics.program_percentage.humanities':'Liberal Arts And Sciences, General Studies And Humanitie',
    '2014.academics.program_percentage.library': 'Library Science',
    '2014.academics.program_percentage.biological': 'Biological And Biomedical Sciences',
    '2014.academics.program_percentage.mathematics':'Mathematics And Statistics',
    '2014.academics.program_percentage.military':'Military Technologies And Applied Sciences',
    '2014.academics.program_percentage.multidiscipline':'Multi/Interdisciplinary Studies',
    '2014.academics.program_percentage.parks_recreation_fitness':'Parks, Recreation, Leisure, And Fitness Studies',
    '2014.academics.program_percentage.philosophy_religious':'Philosophy And Religious Studie',
    '2014.academics.program_percentage.theology_religious_vocation':'Theology And Religious Vocations',
    '2014.academics.program_percentage.physical_science':'Physical Sciences',
    '2014.academics.program_percentage.science_technology':'Science Technologies/Technician',
    '2014.academics.program_percentage.psychology': 'Psychology',
    '2014.academics.program_percentage.security_law_enforcement': 'Homeland Security, Law Enforcement, Firefighting And Related Protective Service',
    '2014.academics.program_percentage.public_administration_social_service':'Public Administration And Social Service Profession',
    '2014.academics.program_percentage.social_science':'Social Sciences',
    '2014.academics.program_percentage.construction':'Construction Trades',
    '2014.academics.program_percentage.mechanic_repair_technology':'Mechanic And Repair Technologies/Technicians',
    '2014.academics.program_percentage.precision_production': 'Precision Production',
    '2014.academics.program_percentage.transportation': 'Transportation And Materials Moving',
    '2014.academics.program_percentage.visual_performing':'Visual And Performing Arts',
    '2014.academics.program_percentage.health':'Health Professions And Related Programs',
    '2014.academics.program_percentage.business_marketing':'Business, Management, Marketing, And Related Support Service',
    '2014.academics.program_percentage.history': 'History'

  }
  degree_models = {}
  degree_private_counts = {}
  degree_public_counts = {}

  url = 'https://api.data.gov/ed/collegescorecard/v1/schools.json?school.degrees_awarded.highest=4&school.ownership=1,2&school.degrees_awarded.predominant=3&per_page=100&_fields=school.state,school.name,school.school_url,school.ownership,2014.cost.attendance.academic_year,2014.student.size,\
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
  
  jsonData = 0
  resultList = []
  for i in range(0,15):
    response = urlopen(url + "&page=" + str(i))
    jsonData = json.load(response)
    resultList = resultList + jsonData["results"] 

  json = resultList

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

  for i in json:

    state_name = i["school.state"]
    state = next((state for state in states if state.name == state_name),None)

    if i["2014.cost.attendance.academic_year"] is None:
      cost = 0
    else:
      cost = i["2014.cost.attendance.academic_year"] 

    if (state):
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
    i.name = states_abbrevs[i.name]
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

  for i in json:

    uni = University()
    uni.name = i["school.name"]
    if i["school.ownership"] == 1:
      uni.is_public = True
    else:
      uni.is_public = False

    uni.website_URL = str(i["school.school_url"])
    uni.academic_cost = i["2014.cost.attendance.academic_year"]
    uni.num_students = i["2014.student.size"]
    
    state_name = states_abbrevs[i["school.state"]]
    state = next((state for state in states if state.name == state_name),None)
    if (state):
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
          degree_models[degree_code].num_percent_public += i[degree_code]
        else:
          degree_private_counts[degree_code] += 1
          degree_models[degree_code].num_percent_private += i[degree_code]

    db.session.add(uni)

  for degree_code, degree in degree_models.items():
    degree.num_public_offer = degree_public_counts[degree_code]
    degree.num_private_offer = degree_private_counts[degree_code]


    if (degree.num_public_offer == 0):
      degree.num_percent_public = 0
    else:
      degree.num_percent_public = floored_percentage(degree.num_percent_public / degree.num_public_offer, 2)

    if (degree.num_private_offer == 0):
      degree.num_percent_private = 0
    else:
      degree.num_percent_private = floored_percentage(degree.num_percent_private / degree.num_private_offer,2)
    db.session.add(degree)

  db.session.commit()