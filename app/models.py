"""
Model.py is used to represent all the tables in sqlalchemy database.
"""

from sqlalchemy import Table, Column, Float, Integer, String, Boolean, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class University(Base):
    """
    Created 5 column attributes of University model: 
    1. Name of the university 
    2. Number of students
    3. Whether school is public or not
    4. URL of school's website
    5. Academic cost
    Linked the University model to the DegreesUniversities model to check all the degrees offered by the university
    Linked the University model to the State model to check what state a university is from
    """
    __tablename__ = 'university'
    id = Column(Integer, primary_key=True)

    name = Column(String)
    num_students = Column(Integer)
    is_public = Column(Boolean)
    website_URL = Column(String)
    academic_cost = Column(Integer)
    degrees = relationship("DegreesUniversities", back_populates="university")

    state_id = Column(Integer, ForeignKey('state.id'))

    def __repr__(self):
        return "<University(name={}, num_students={}, is_public={}, website_URL={}, academic_cost={}"\
            .format(self.name, self.num_students, self.is_public, self.website_URL, self.academic_cost)


class State(Base):
    """
    Created 5 column attributes of State model: 
    1. Name of state 
    2. Region state is located
    3. Average public tuition in the state
    4. Average private tuition in the state
    5. Number of colleges in the state
    Linked the State model to to the University model to find all the universities in a given state
    """
    __tablename__ = 'state'
    id = Column(Integer, primary_key=True)

    name = Column(String)
    region = Column(String)
    average_public_tuition = Column(Integer)
    average_private_tuition = Column(Integer)
    number_colleges = Column(Integer)
    universities = relationship('University', backref='state')

    def __repr__(self):
        return "<State(name={}, region={}, average_public_tuition={}, average_private_tuition={}, number_colleges={}"\
            .format(self.name, self.region, self.average_public_tuition, self.average_private_tuition, self.number_colleges)


class Degree(Base):
    """
    Created 5 column attributes of Degree model: 
    1. Name of degree 
    2. Number of public schools that offer degree
    3. Number of private schools that offer degree
    4. Percent of public schools that offer degree
    5. Percent of private schools that offer degree
    Linked Degree model to DegreeUniversities model to check all the universities that offer the degree
    """
    __tablename__ = 'degree'
    id = Column(Integer, primary_key=True)

    name = Column(String)
    num_public_offer = Column(Integer)
    num_private_offer = Column(Integer)
    num_percent_public = Column(Float)
    num_percent_private = Column(Float)
    universities = relationship("DegreesUniversities", back_populates="degree")

    def __repr__(self):
        return "<Degree(name={}, num_public_offer={}, num_private_offer={}\
            , num_percent_public= {}, num_percent_private={}".format(self.name, self.num_public_offer,\
                self.num_private_offer, self.num_percent_public, self.num_percent_private)


class DegreesUniversities(Base):
    """
    Helps link the Degrees model and University model together to help check all the degrees 
    offered by a university and all the universities that offer a degree. Got help from this reference many to many:
    http://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html#many-to-many
    """
    __tablename__ = 'degreesUniversities'

    id = Column(Integer, primary_key=True)

    university_id = Column(Integer, ForeignKey("University.id"))
    degree_id = Column(Integer, ForeignKey("Degree.id"))

    degree = relationship("Degree", back_populates = "universities")
    university = relationship("University", back_populates = "degrees")

    def __repr__(self):
        return "<DegreesUniversities(degree_name={})>".format(self.degree_name)


if __name__ == '__main__':
    engine = create_engine("")
    Base.metadata.create_all(engine)