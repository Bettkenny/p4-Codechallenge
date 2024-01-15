from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'hero'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    power = db.Column(db.String(255))
    description = db.Column(db.Text)

    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError("Name cannot be empty.")
        if len(name) > 255:
            raise ValueError("Name cannot exceed 255 characters.")
        return name

    @validates('power')
    def validate_power(self, key, power):
        if power and len(power) > 255:
            raise ValueError("Power cannot exceed 255 characters.")
        return power
    
    @validates('description')
    def validate_description(self, key, description):
        if description and len(description) > 800:
            raise ValueError("Description cannot exceed 800 characters.")
        return description

    def __repr__(self):
        return f'<Hero(id={self.id}, name={self.name}, power={self.power})>'


class Power(db.Model):
    __tablename__ = 'power'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    description = db.Column(db.Text)

    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError("Name cannot be empty.")
        if len(name) > 255:
            raise ValueError("Name cannot exceed 255 characters.")
        return name

    @validates('description')
    def validate_description(self, key, description):
        if description and len(description) > 800:
            raise ValueError("Description cannot exceed 800 characters.")
        return description

    def __repr__(self):
        return f'<Power(id={self.id}, name={self.name})>'


class HeroPower(db.Model):
    __tablename__ = 'hero_power'

    id = db.Column(db.Integer, primary_key=True)
    hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('power.id'), nullable=False)
    strength = db.Column(db.Integer)

    @validates('strength')
    def validate_strength(self, key, strength):
        if strength < 0 or strength > 100:
            raise ValueError("Strength must be between 0 and 100.")
        return strength

    def __repr__(self):
        return f'<HeroPower(id={self.id}, hero_id={self.hero_id}, power_id={self.power_id}, strength={self.strength})>'
