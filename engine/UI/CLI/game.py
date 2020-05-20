from engine.server.economy import Economy
from engine.UI.CLI.windows import Windows

class Game(Windows):
    commands = None
    class Commands:
        pass

    @classmethod
    def make_hello_and_commands(_class_, UI_class):
        _class_.hello = UI_class.content.game.hello
        _class_.commands = []

    def __init__(self, UI_class, user):
        super().__init__(UI_class)
        self.user = user
        self.economy = Economy(self.user.user_id)
    def onexit(self):
        print(self.content.game.logout)

    def windows_action(self):
        self.economy.reload()
        self.economy.display(self.UI)


    # def search_planet(self, ):