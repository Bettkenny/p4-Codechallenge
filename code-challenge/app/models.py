from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'hero'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255),nullable=False)
    power = db.Column(db.String(255))
    description = db.Column(db.Text)

    def __repr__(self):
        return f'<Hero(id={self.id}, name={self.name}, power={self.power})>'


    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError("Name cannot be empty.")
        if len(name) > 255:
            raise ValueError("Name cannot exceed 255 characters.")
        return name
    
    @validates('power')
    def validate_power(self, key, power):
        if power and len(power) >255:
            raise  ValueError("Power cannot exceed 255 characters")
        return power
    
    @validates('description')
    def validate_description(self, key, description):
        if description and len(description) > 800:
            raise ValueError ("Description cannot exceed 800 characters.")
        return description
    def __repr__(self):
        return f'<Hero(id={self.id}, name={self.name}, power={self.power})>'
# add any models you may need. 