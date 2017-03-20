from sqlalchemy import Table, Column, Float, Integer, String, Boolean, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class University(Base):
    __tablename__ = 'university'
    id = Column(Integer, primary_key=True)

    name = Column(String)
    num_students = Column(Integer)
    is_public = Column(Boolean)
    website_URL = Column(String)
    academic_cost = Column(Integer)
    """
    # Relationships for recipes
    cuisine_id = Column(Integer, ForeignKey('cuisine.id'))
    cuisine = relationship("Cuisine", back_populates="recipes")
    ingredientInfos = relationship("IngredientInfo", back_populates="recipe")

    # Override __repr__ to display object properly
    def __repr__(self):
        return "<Recipe(title='%s', readyInMinutes='%i', servings='%i', calories='%i', steps='%s', numberOfSteps='%i')>" % (
            self.title, self.readyInMinutes, self.servings, self.calories, self.steps, self.numberOfSteps)
    """
    degrees = relationship("DegreesUniversities", back_populates="university")

    state_id = Column(Integer, ForeignKey('state.id'))

    def __repr__(self):
        return "<University(name={}, num_students={}, is_public={}, website_URL={}, academic_cost={}"\
            .format(self.name, self.num_students, self.is_public, self.website_URL, self.academic_cost)

class State(Base):
    __tablename__ = 'state'
    id = Column(Integer, primary_key=True)

    name = Column(String)
    region = Column(String)
    average_public_tuition = Column(Integer)
    average_private_tuition = Column(Integer)
    number_colleges = Column(Integer)
    """
    # Relationships for ingredients
    recipe = relationship("Recipe", back_populates="ingredientInfos")
    ingredient = relationship("Ingredient", back_populates="ingredientInfos")

    # Override __repr__ to display object properly
    def __repr__(self):
        return "<IngredientInfo(name='%s', fullName='%s')>" % (
            self.name, self.fullName)
    """
    universities = relationship('University', backref='state')

    def __repr__(self):
        return "<State(name={}, region={}, average_public_tuition={}, average_private_tuition={}, number_colleges={}"\
            .format(self.name, self.region, self.average_public_tuition, self.average_private_tuition, self.number_colleges)

class Degree(Base):
    __tablename__ = 'degree'
    id = Column(Integer, primary_key=True)

    name = Column(String)
    num_public_offer = Column(Integer)
    num_private_offer = Column(Integer)
    num_percent_public = Column(Float)
    num_percent_private = Column(Float)
    """
    # Relationships for ingredients
    ingredientInfos = relationship("IngredientInfo", back_populates="ingredient")

    # Override __repr__ to display object properly
    def __repr__(self):
        return "<Ingredient(title='%s', serving_size='%s', total_weight='%s', brand='%s', category='%s')>" % (
            self.title, self.serving_size, self.total_weight, self.brand, self.category)
    """
    universities = relationship("DegreesUniversities", back_populates="degree")

    def __repr__(self):
        return "<Degree(name={}, num_public_offer={}, num_private_offer={}\
            , num_percent_public= {}, num_percent_private={}".format(self.name, self.num_public_offer,\
                self.num_private_offer, self.num_percent_public, self.num_percent_private)

# Reference many to many: http://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html#many-to-many
class DegreesUniversities(Base):
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