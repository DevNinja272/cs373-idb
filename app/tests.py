from unittest import main, TestCase
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from models import University, State, Degree, DegreesUniversities, db
from config import test_db_config
from app import app
import json


class TestModels (TestCase):

    def setUp(self):
        self.engine = create_engine("postgresql://" + test_db_config['user'] + ":" + test_db_config['pass'] + "@" + test_db_config['host'] + "/" + test_db_config['db_name'])
        self.sess = sessionmaker(bind = self.engine)
        db.metadata.create_all(self.engine)
        app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://" + test_db_config['user'] + ":" + test_db_config['pass'] + "@" + test_db_config['host'] + "/" + test_db_config['db_name']
        
        # from https://damyanon.net/flask-series-testing/
        # creates a test client
        self.app = app.test_client()

        # propagate the exceptions to the test client
        self.app.testing = True 



    def test_university_1(self):
        session = self.sess()

        university = University(name='Test University', num_students=3, is_public=True, website_URL='http://test.safsfa', academic_cost=34564)
        session.add(university)
        session.commit()
        result_first = session.query(University).order_by(University.id.desc()).first()
        self.assertEqual(result_first.name, 'Test University')
        session.delete(university)
        session.commit()

    def test_university_2(self):
        session = self.sess()
        pre_add_count = session.query(University).count()
        university_1 = University(name='Test University 1', num_students=3, is_public=True, website_URL='http://test.safsfa', academic_cost=34564)
        university_2 = University(name='Test University 2', num_students=3, is_public=True, website_URL='http://test.safsfa', academic_cost=34564)
        session.add(university_1)
        session.add(university_2)
        session.commit()

        result_count = session.query(University).count()
        self.assertEqual(result_count, pre_add_count+2)
        session.delete(university_1)
        session.delete(university_2)
        session.commit()

    def test_university_3(self):
        session = self.sess()

        university_1 = University(name='Test University 1', num_students=3, is_public=True, website_URL='http://test.safsfa', academic_cost=34564)
        state_1 = State(name='Alabama', region='South', average_public_cost=5, average_private_cost=109, number_colleges=1)
        university_1.state = state_1
        session.add(university_1)
        session.add(state_1)
        session.commit()

        result = session.query(University).order_by(University.id.desc()).first()
        self.assertEqual(result.state.name, state_1.name)
        session.delete(university_1)
        session.delete(state_1)
        session.commit()

    def test_state_1(self):
        session = self.sess()

        state = State(name='Alabama', region='South', average_public_cost=5, average_private_cost=109, number_colleges=1)
        session.add(state)
        session.commit()
        result_first = session.query(State).order_by(State.id.desc()).first()
        self.assertEqual(result_first.name, 'Alabama')
        session.delete(state)
        session.commit()

    def test_state_2(self):
        session = self.sess()
        pre_add_count = session.query(State).count()
        state_1 = State(name='Alabama', region='South', average_public_cost=5, average_private_cost=109, number_colleges=1)
        state_2 = State(name='Texas', region='South', average_public_cost=5, average_private_cost=109, number_colleges=1)
        session.add(state_1)
        session.add(state_2)
        session.commit()
        result_count = session.query(State).count()
        self.assertEqual(result_count, pre_add_count+2)

        session.delete(state_1)
        session.commit()

        result_count = session.query(State).count()
        self.assertEqual(result_count, pre_add_count+1)
        session.delete(state_2)
        session.commit()

    def test_state_3(self):
        session = self.sess()

        university_1 = University(name='Test University 1', num_students=3, is_public=True, website_URL='http://test.safsfa', academic_cost=34564)
        university_2 = University(name='Test University 2', num_students=3, is_public=True, website_URL='http://test.safsfa', academic_cost=34564)
        state_1 = State(name='Alabama', region='South', average_public_cost=5, average_private_cost=109, number_colleges=1)
        university_1.state = state_1
        university_2.state = state_1
        session.add(university_1)
        session.add(university_2)
        session.add(state_1)
        session.commit()

        result_state = session.query(State).order_by(State.id.desc()).first()
        self.assertEqual(len(result_state.universities), 2)
        session.delete(university_1)
        session.delete(university_2)
        session.delete(state_1)
        session.commit()

    def test_degree_1(self):
        session = self.sess()

        degree = Degree(name='Degree', num_public_offer=3, num_private_offer=3, num_percent_public=4.03, num_percent_private=3.234)
        session.add(degree)
        session.commit()
        result_first = session.query(Degree).order_by(Degree.id.desc()).first()
        self.assertEqual(result_first.name, 'Degree')
        session.delete(degree)
        session.commit()

    def test_degree_2(self):
        session = self.sess()
        pre_add_count = session.query(Degree).count()
        degree_1 = Degree(name='Degree 1', num_public_offer=3, num_private_offer=3, num_percent_public=4.03, num_percent_private=3.234)
        degree_2 = Degree(name='Degree 2', num_public_offer=3, num_private_offer=3, num_percent_public=4.03, num_percent_private=3.234)
        session.add(degree_1)
        session.add(degree_2)
        session.commit()
        result_count = session.query(Degree).count()
        self.assertEqual(result_count, pre_add_count+2)
        session.delete(degree_1)
        session.delete(degree_2)
        session.commit()

    def test_degree_3(self):
        session = self.sess()
        pre_add_count = session.query(Degree).count()
        degree_1 = Degree(name='Degree 1', num_public_offer=3, num_private_offer=3, num_percent_public=4.03, num_percent_private=3.234)
        degree_2 = Degree(name='Degree 2', num_public_offer=3, num_private_offer=3, num_percent_public=4.03, num_percent_private=3.234)
        session.add(degree_1)
        session.add(degree_2)
        session.commit()
        result_count = session.query(Degree).count()
        self.assertEqual(result_count, pre_add_count+2)

        session.delete(degree_1)
        session.commit()
        result_count = session.query(Degree).count()
        self.assertEqual(result_count, pre_add_count+1)

        session.delete(degree_2)
        session.commit()

    def test_degrees_universities_1(self):
        session = self.sess()

        university_1 = University(name='Test University 1', num_students=3, is_public=True, website_URL='http://test.safsfa', academic_cost=34564)
        degree_1 = Degree(name='Degree 1', num_public_offer=3, num_private_offer=3, num_percent_public=4.03, num_percent_private=3.234)
        degrees_universities = DegreesUniversities()
        degrees_universities.university = university_1
        degree_1.universities.append(degrees_universities)
        session.add(university_1)
        session.add(degree_1)
        session.add(degrees_universities)
        session.commit()

        result = session.query(University).order_by(University.id.desc()).first()
        self.assertEqual(result.degrees[0].degree.name, 'Degree 1')
        session.delete(university_1)
        session.delete(degree_1)
        session.delete(degrees_universities)
        session.commit()

    def test_degrees_universities_2(self):
        session = self.sess()

        university_1 = University(name='Test University 1', num_students=3, is_public=True, website_URL='http://test.safsfa', academic_cost=34564)
        university_2 = University(name='Test University 2', num_students=3, is_public=True, website_URL='http://test.safsfa', academic_cost=34564)
        
        degree_1 = Degree(name='Degree 1', num_public_offer=3, num_private_offer=3, num_percent_public=4.03, num_percent_private=3.234)
        degrees_universities_1 = DegreesUniversities()
        degrees_universities_2 = DegreesUniversities()

        degrees_universities_1.university = university_1
        degrees_universities_2.university = university_2

        degree_1.universities.append(degrees_universities_1)
        degree_1.universities.append(degrees_universities_2)

        session.add(university_1)
        session.add(university_2)
        session.add(degree_1)
        session.add(degrees_universities_1)
        session.add(degrees_universities_2)
        session.commit()

        result = session.query(Degree).order_by(Degree.id.desc()).first()
        self.assertEqual(len(result.universities), 2)
        session.delete(university_1)
        session.delete(university_2)      
        session.delete(degree_1)
        session.delete(degrees_universities_1)
        session.delete(degrees_universities_2)

        session.commit()

    def test_degrees_universities_3(self):
        session = self.sess()

        university_1 = University(name='Test University 1', num_students=3, is_public=True, website_URL='http://test.safsfa', academic_cost=34564)
        
        degree_1 = Degree(name='Degree 1', num_public_offer=3, num_private_offer=3, num_percent_public=4.03, num_percent_private=3.234)
        degree_2 = Degree(name='Degree 2', num_public_offer=3, num_private_offer=3, num_percent_public=4.03, num_percent_private=3.234)
        
        degrees_universities_1 = DegreesUniversities()
        degrees_universities_2 = DegreesUniversities()

        degrees_universities_1.university = university_1
        degrees_universities_2.university = university_1

        degree_1.universities.append(degrees_universities_1)
        degree_2.universities.append(degrees_universities_2)

        session.add(university_1)
        session.add(degree_1)
        session.add(degree_2)
        session.add(degrees_universities_1)
        session.add(degrees_universities_2)
        session.commit()

        result = session.query(University).order_by(University.id.desc()).first()
        self.assertEqual(len(result.degrees), 2)
        session.delete(university_1)
        session.delete(degree_1)
        session.delete(degree_2)      
        session.delete(degrees_universities_1)
        session.delete(degrees_universities_2)
        session.commit()

    def test_get_home(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200) 

    def test_get_single_uni_1(self):
        session = self.sess()

        university = University(name='Test University', num_students=3, is_public=True, website_URL='http://test.safsfa', academic_cost=34564)
        session.add(university)
        session.commit()

        result = self.app.get('/api/universities/1')
        self.assertEqual(result.status_code, 200) 

        session.delete(university)
        session.commit()
        

    def test_get_single_uni_2(self):
        session = self.sess()

        university = University(name='Test University', num_students=3, is_public=True, website_URL='http://test.safsfa', academic_cost=34564)
        session.add(university)
        session.commit()

        result = self.app.get('/api/universities/1')
        result = json.loads(result.data.decode('utf-8'))
        self.assertIn("university", result)
        self.assertIn("academic_cost", result["university"])
        self.assertIn("state_name", result["university"])

        session.delete(university)
        session.commit()

    def test_get_all_unis_1(self):
        session = self.sess()

        university = University(name='Test University', num_students=3, is_public=True, website_URL='http://test.safsfa', academic_cost=34564)
        session.add(university)
        session.commit()

        result = self.app.get('/api/universities')
        self.assertEqual(result.status_code, 200) 

        session.delete(university)
        session.commit()


    def test_get_all_unis_2(self):
        session = self.sess()

        university = University(name='Test University', num_students=3, is_public=True, website_URL='http://test.safsfa', academic_cost=34564)
        session.add(university)
        session.commit()

        result = self.app.get('/api/universities')
        result = json.loads(result.data.decode('utf-8'))
        self.assertIn("universities", result)

        session.delete(university)
        session.commit()

    def test_get_single_degree_1(self):
        result = self.app.get("api/degrees/1")
        self.assertEqual(result.status_code, 200) 

    def test_get_single_degree_2(self):
        result = self.app.get("api/degrees/1")
        result = json.loads(result.data.decode("utf-8"))
        self.assertIn("degree", result)
        self.assertIn("universities", result["degree"])
        self.assertIn("id", result["degree"])

    def test_get_all_degrees_1(self):
        result = self.app.get('/api/degrees')
        self.assertEqual(result.status_code, 200) 

    def test_get_all_degrees_2(self):
        result = self.app.get('/api/degrees')
        result = json.loads(result.data.decode('utf-8'))
        self.assertIn("degrees", result) 

    def test_get_single_state_1(self):
        result = self.app.get("api/states/1")
        self.assertEqual(result.status_code, 200) 

    def test_get_single_state_2(self):
        result = self.app.get("api/states/1")
        result = json.loads(result.data.decode("utf-8"))
        self.assertIn("state", result)
        self.assertIn("universities", result["state"])
        self.assertIn("id", result["state"])

    def test_get_all_states_1(self):
        result = self.app.get('/api/states')
        self.assertEqual(result.status_code, 200) 

    def test_get_all_states_2(self):
        result = self.app.get('/api/states')
        result = json.loads(result.data.decode('utf-8'))
        self.assertIn("states", result) 

    def test_search_1(self):
        result = self.app.get('/api/search?query=tx')
        self.assertEqual(result.status_code, 200) 

    def test_search_2(self):
        result = self.app.get('/api/search?query=texas')
        self.assertEqual(result.status_code, 200) 

    def test_search_3(self):
        result = self.app.get('/api/search?query=CA')
        self.assertEqual(result.status_code, 200)

    def test_search_4(self):
        result = self.app.get('/api/search?query=Theology')
        self.assertEqual(result.status_code, 200)

    def test_search_4(self):
        result = self.app.get('/api/search')
        result = json.loads(result.data.decode('utf-8'))
        self.assertIn("Error", result)


    





if __name__ == "__main__":
    main()