from engine.lang import Lang

class User:
    @staticmethod
    def login(username, password):
        # search in db
        user_id = None
        user_id = 0
        if user_id is not None:
            return User(user_id)
        else:
            return True

    def __init__(self, id):
        self.id = id
    def play(self):
        print("Play")
class Registration:
    def __init__(self, username, password):
        print("registration for", username, password)