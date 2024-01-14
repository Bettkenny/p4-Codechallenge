#!/usr/bin/env python3

from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate

from models import db, Hero, Power, HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return ''

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    heroes_list = [{'id': hero.id, 'name': hero.name, 'power': hero.power, 'description': hero.description} for hero in heroes]
    return jsonify(heroes_list)


@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get_or_404(id)

    new_description = request.json.get('description')

    
    if new_description is not None:
        power.description = new_description
        db.session.commit()

    updated_power_data = {
        'id': power.id,
        'name': power.name,
        'description': power.description
    }

    return jsonify(updated_power_data)@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    hero_id = request.json.get('hero_id')
    power_id = request.json.get('power_id')
    strength = request.json.get('strength')

    if hero_id is None or power_id is None or strength is None:
        return jsonify({'error': 'Missing required fields'}), 400

    hero = Hero.query.get(hero_id)
    power = Power.query.get(power_id)

    if hero is None or power is None:
        return jsonify({'error': 'Hero or Power not found'}), 404

    
    hero_power = HeroPower(hero=hero, power=power, strength=strength)
    db.session.add(hero_power)
    db.session.commit()

   
    created_hero_power_data = {
        'id': hero_power.id,
        'hero_name': hero.name,
        'power_name': power.name,
        'strength': hero_power.strength
    }

    return jsonify(created_hero_power_data), 201  



if __name__ == '__main__':
    app.run(port=5555)
