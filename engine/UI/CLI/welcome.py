# -*- coding: utf-8 -*-
from engine.models.user import User
from engine.UI.CLI.windows import Windows
from engine.UI.CLI.game import Game
import getpass
from engine.lang import Lang
class Welcome(Windows):
    # language keep in Welcome only
    class Commands:
        @staticmethod
        def login(UI_class):
            Windows.header(UI_class.content.login.hello)
            username = input(Lang.prompt.format(UI_class.content.login.username_prompt))
            password = getpass.getpass(Lang.prompt.format(UI_class.content.login.password_prompt))
            user = User.login(username, password)
            if user:
                Game.display_windows(UI_class, user)
            else:
                print(UI_class.content.login.failed)
            return True
        @staticmethod
        def register(UI_class):
            Windows.header(UI_class.content.register.hello)
            username = input(Lang.prompt.format(UI_class.content.register.username_prompt))
            password = input(Lang.prompt.format(UI_class.content.register.password_prompt))
            user_id = User.registration(username, password)
            if user_id:
                print(Lang.message_value.format(UI_class.content.register.ok, username))
                user = User(user_id)
                user.receive_planet()
                Game.display_windows(Welcome, user)
            else:
                print(Lang.message_value.format(UI_class.content.register.fail, username))
            return True

    @classmethod
    def make_hello_and_commands(_class_, UI_class):
        _class_.hello = UI_class.content.welcome.hello
        _class_.commands = [
            {UI_class.content.login.command:
                {
                    "desc": UI_class.content.login.desc,
                    "action": Welcome.Commands.login
                }
            },
            {UI_class.content.register.command:
                {
                    "desc": UI_class.content.register.desc,
                    "action": Welcome.Commands.register
                }
            }
        ]
    def onexit(self):
        print(self.content.welcome.farewell)