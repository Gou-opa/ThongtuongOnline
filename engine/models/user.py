from configs import USER_TABLE_NAME, ECONOMY_TABLE_NAME
from engine.db.mysql import db
from engine.server.nature import Planet


class User:
    table_name = USER_TABLE_NAME
    @staticmethod
    def login(username, password):
        # search in db
        result = db.new_execute(
            "SELECT user_id FROM {} WHERE username=%s and password=%s".format(User.table_name),
            (username, password)
        ).fetchone()
        if result is not None:
            return User(result['user_id'])
        else:
            return None
    def __init__(self, user_id):
        self.user_id = user_id

    def receive_planet(self):
        planet = Planet.pick()
        planet.own(self.user_id)
    @staticmethod
    def registration(username, password):
        try:
            cursor = db.new_execute("INSERT INTO {} (username, password) VALUES (%s, %s)".format(User.table_name), (username, password))
            user_id = cursor.lastrowid
            db.new_execute("INSERT INTO {} (user_id) VALUES (%s)".format(ECONOMY_TABLE_NAME),
                           (user_id,))
            return user_id
        except Exception as e:
            raise e
            return False