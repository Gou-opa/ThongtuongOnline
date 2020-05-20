from configs import *
import random, math
from engine.db.mysql import db
class Resource:
    @staticmethod
    def creation():
        for i in range(PLANET_SPAWN_RATE):
            Planet.born()

class Planet(Resource):
    table_name = PLANET_TABLE_NAME
    def __init__(self, planet_id=None, type=None):
        print("INIT", planet_id)
        if type: # create new planet
            planet_info = PLANET_TYPE[type]
            s_range = planet_info['size']
            radius = round(random.uniform(s_range[0], s_range[1])*EARTH_RADIUS)
            square = round(4*math.pi*radius**2)
            population = round((square/EARTH_SQUARE)*EARTH_AC_POPULATION)
            cost = square*1000 # 1000$ per km2
            print(type, radius, square, population, cost)
            db.new_execute(
                "INSERT INTO {} (population,type, radius, cost) VALUES (%s,%s,%s, %s)".format(Planet.table_name),
                (population, type, radius, cost)
            )
        else:
            self.planet_id = planet_id
            self.user_id = self.population = self.increase_rate = self.gdp = self.cpi = self.type = self.radius = self.cost = None
            self.load()
    def load(self):
        data = tuple(
            db.new_execute(
                "SELECT * FROM {} WHERE planet_id = %s".format(PLANET_TABLE_NAME),
                (self.planet_id,)
            ).fetchone().values()
        )
        self.planet_id, self.user_id, self.population, self.increase_rate, self.gdp, self.cpi, self.type, self.radius, self.cost = data
    @staticmethod
    def pick():
        planet_id = db.new_execute(
            "SELECT planet_id FROM {} WHERE user_id is NULL ORDER BY RAND() LIMIT 1".format(PLANET_TABLE_NAME)
        ).fetchone()['planet_id']
        print("Gift", planet_id)
        return Planet(planet_id=planet_id)

    def own(self, user_id):
        print(self.planet_id)
        db.new_execute("UPDATE {} SET user_id = %s WHERE planet_id = %s".format(PLANET_TABLE_NAME), (user_id, self.planet_id))
    @staticmethod
    def born():
        universe = []
        for type, info in PLANET_TYPE.items():
            for i in range(info['occurance']):
                universe.append(type)
        Planet(type=random.choice(universe))