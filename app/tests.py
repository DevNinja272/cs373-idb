from unittest import main, TestCase

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import University, State, Degree
from config import db


class TestModels (TestCase):

    def setUp(self):
        self.engine = create_engine("postgresql://" + db['user'] + ":" + db['pass'] + "@" + db['host'] + "/" + db['db_name'])
        self.sess = sessionmaker(bind=self.engine)
        

    def test_university_1(self):
        session = self.sess()

        university = University(name='Test University', num_students=3, is_public=True, website_URL='http://test.safsfa', academic_cost=34564)
        session.add(university)
        session.commit()
        result_first = session.query(University).first()
        self.assertEqual(result_first.name, 'Test University')
        session.delete(university)
        session.commit()

    def test_university_2(self):
        session = self.sess()

        university_1 = University(name='Test University 1', num_students=3, is_public=True, website_URL='http://test.safsfa', academic_cost=34564)
        university_2 = University(name='Test University 2', num_students=3, is_public=True, website_URL='http://test.safsfa', academic_cost=34564)
        session.add(university_1)
        session.add(university_2)
        session.commit()

        result_count = session.query(University).count()
        self.assertEqual(result_count, 2)
        session.delete(university_1)
        session.delete(university_2)
        session.commit()

    def test_university_3(self):
        session = self.sess()

        university_1 = University(name='Test University 1', num_students=3, is_public=True, website_URL='http://test.safsfa', academic_cost=34564)
        state_1 = State(name='Alabama', region='South', average_public_tution=5, average_private_tuition=109, number_colleges=1)
        university_1.state = state_1
        session.add(university_1)
        session.add(state_1)
        session.commit()

        result = session.query(University).first()
        self.assertEqual(result.state.name, state_1.name)
        session.delete(university_1)
        session.delete(state_1)
        session.commit()

    def test_state_1(self):
        session = self.sess()

        state = State(name='Alabama', region='South', average_public_tution=5, average_private_tuition=109, number_colleges=1)
        session.add(state)
        session.commit()
        result_first = session.query(State).first()
        self.assertEqual(result_first.name, 'Alabama')
        session.delete(state)
        session.commit()

    def test_state_2(self):
        session = self.sess()

        state_1 = State(name='Alabama', region='South', average_public_tution=5, average_private_tuition=109, number_colleges=1)
        state_2 = State(name='Texas', region='South', average_public_tution=5, average_private_tuition=109, number_colleges=1)
        session.add(state_1)
        session.add(state_2)
        session.commit()
        result_count = session.query(State).count()
        self.assertEqual(result_count, 2)

        session.delete(state_1)
        session.commit()

        result_count = session.query(State).count()
        self.assertEqual(result_count, 1)
        session.delete(state_2)
        session.commit()

    def test_state_3(self):
        session = self.sess()

        university_1 = University(name='Test University 1', num_students=3, is_public=True, website_URL='http://test.safsfa', academic_cost=34564)
        university_2 = University(name='Test University 2', num_students=3, is_public=True, website_URL='http://test.safsfa', academic_cost=34564)
        state_1 = State(name='Alabama', region='South', average_public_tution=5, average_private_tuition=109, number_colleges=1)
        university_1.state = state_1
        university_2.state = state_1
        session.add(university_1)
        session.add(university_2)
        session.add(state_1)
        session.commit()

        result_state = session.query(State).first()
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
        result_first = session.query(Degree).first()
        self.assertEqual(result_first.name, 'Degree')
        session.delete(degree)
        session.commit()

    def test_degree_2(self):
        session = self.sess()

        degree_1 = Degree(name='Degree 1', num_public_offer=3, num_private_offer=3, num_percent_public=4.03, num_percent_private=3.234)
        degree_2 = Degree(name='Degree 2', num_public_offer=3, num_private_offer=3, num_percent_public=4.03, num_percent_private=3.234)
        session.add(degree_1)
        session.add(degree_2)
        session.commit()
        result_count = session.query(Degree).count()
        self.assertEqual(result_count, 2)
        session.delete(degree_1)
        session.delete(degree_2)
        session.commit()

    def test_degree_3(self):
        session = self.sess()

        degree_1 = Degree(name='Degree 1', num_public_offer=3, num_private_offer=3, num_percent_public=4.03, num_percent_private=3.234)
        degree_2 = Degree(name='Degree 2', num_public_offer=3, num_private_offer=3, num_percent_public=4.03, num_percent_private=3.234)
        session.add(degree_1)
        session.add(degree_2)
        session.commit()
        result_count = session.query(Degree).count()
        self.assertEqual(result_count, 2)

        session.delete(degree_1)
        session.commit()
        result_count = session.query(Degree).count()
        self.assertEqual(result_count, 1)

        session.delete(degree_2)
        session.commit()

    def test_degrees_universities_1(self):
        session = self.sess()

        university_1 = University(name='Test University 1', num_students=3, is_public=True, website_URL='http://test.safsfa', academic_cost=34564)
        degree_1 = Degree(name='Degree 1', num_public_offer=3, num_private_offer=3, num_percent_public=4.03, num_percent_private=3.234)
        degrees_universities = DegreesUniversities()
        degrees_universities.university = [university_1]
        degree_1.universities.append(degrees_universities)
        session.add(university_1)
        session.add(degree_1)
        session.add(degrees_universities)
        session.commit()

        result = session.query(University).first()
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
        degrees_universities = DegreesUniversities()
        degrees_universities.university = [university_1, university_2]
        degree_1.universities.append(degrees_universities)
        session.add(university_1)
        session.add(university_2)
        session.add(degree_1)
        session.add(degrees_universities)
        session.commit()

        result = session.query(Degree).first()
        self.assertEqual(len(result.degrees[0].university), 2)
        session.delete(university_1)
        session.delete(university_2)      
        session.delete(degree_1)
        session.delete(degrees_universities)
        session.commit()

    def test_degrees_universities_3(self):
        session = self.sess()

        university_1 = University(name='Test University 1', num_students=3, is_public=True, website_URL='http://test.safsfa', academic_cost=34564)
        
        degree_1 = Degree(name='Degree 1', num_public_offer=3, num_private_offer=3, num_percent_public=4.03, num_percent_private=3.234)
        degree_2 = Degree(name='Degree 2', num_public_offer=3, num_private_offer=3, num_percent_public=4.03, num_percent_private=3.234)
        
        degrees_universities = DegreesUniversities()
        degrees_universities.university = [university_1]
        degree_1.universities.append(degrees_universities)
        degree_2.universities.append(degrees_universities)

        session.add(university_1)
        session.add(degree_1)
        session.add(degree_2)
        session.add(degrees_universities)
        session.commit()

        result = session.query(University).first()
        self.assertEqual(len(result.degrees[0].degree), 2)
        session.delete(university_1)
        session.delete(degree_1)
        session.delete(degree_2)      
        session.delete(degrees_universities)
        session.commit()

if __name__ == "__main__":
    main()