from unittest import main, TestCase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import University, State, Degrees
from config import test_db

class TestModels (TestCase):

    def test(self):
        self.engine = create_engine("postgresql://" + test_db['USER'] + ":" + test_db['PASSWORD'] + "@" + test_db['IP'] + "/" + test_db['DATABASE'])
        self.sess = sessionmaker(bind=self.engine)

        session = self.sess()
        session.query(Recipe).delete()
        session.query(Ingredient).delete()
        session.query(Cuisine).delete()
        session.commit()

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

    def test_state_2(self):

    def test_state_3(self):

    def test_degrees_1(self):

    def test_degrees_2(self):

    def test_degrees_3(self):

if __name__ == "__main__":
    main()
