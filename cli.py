# -*- coding: utf-8 -*-
from engine.lang import Lang
from engine.user import User, Registration
import utils.utils as utils
from os import system, name
import getpass

class CLI():
    @staticmethod
    def clear():
        if name == 'nt': # for windows
            _ = system('cls')
        else: # for mac and linux(here, os.name is 'posix')
            _ = system('clear')
    language = None
    content = None
    commands = None
    @staticmethod
    def display_window(window_hello, clear=True):
        if clear:
            CLI.clear()
        print(Lang.hello.format(window_hello))
        print(Lang.line_break)
    class Commands:
        @staticmethod
        def login():
            CLI.display_window(CLI.content.cli.login.hello)
            username = input(Lang.prompt.format(CLI.content.cli.login.username_prompt))
            password = getpass.getpass(Lang.prompt.format(CLI.content.cli.login.password_prompt))
            user = User.login(username, password)
            if user:
                user.play()
            else:
                print(CLI.content.cli.login.failed)
            return True
        @staticmethod
        def register():
            CLI.display_window(CLI.content.cli.register.hello)
            username = input(Lang.prompt.format(CLI.content.cli.register.username_prompt))
            password = input(Lang.prompt.format(CLI.content.cli.register.password_prompt))
            return Registration(username, password)
        @staticmethod
        def exit():
            return False
        @staticmethod
        def not_exist():
            print(CLI.content.cli.commands.not_exist)
            return True
        @staticmethod
        def help():
            CLI.display_window(CLI.content.cli.help.hello)
            i = 1
            for command in CLI.commands:
                for action, desc in command.items():
                    print("{}. {}: {}".format(i, action, desc))
                    i += 1
            return True
        @staticmethod
        def change_lang():
            CLI.display_window(CLI.content.cli.language.hello)
            return CLI.change_lang()
    @staticmethod
    def make_commands():
        CLI.commands = [
            {CLI.content.cli.commands.help_command:
                {
                    "desc": CLI.content.cli.commands.help_desc,
                    "action": CLI.Commands.help
                }
            },
            {CLI.content.cli.commands.login_command:
                {
                    "desc": CLI.content.cli.commands.login_desc,
                    "action": CLI.Commands.login
                }
            },
            {CLI.content.cli.commands.register_command:
                {
                    "desc": CLI.content.cli.commands.register_desc,
                    "action": CLI.Commands.register
                }
            },
            {CLI.content.cli.commands.change_lang_command:
                {
                    "desc": CLI.content.cli.commands.change_lang_desc,
                    "action": CLI.Commands.change_lang
                }
            },
            {CLI.content.cli.commands.exit_command:
                {
                    "desc": CLI.content.cli.commands.exit_desc,
                    "action": CLI.Commands.exit
                }
            }

        ]
    def loading(self):
        self.update_language('vi')
    def __init__(self):
        self.loading()
        print(CLI.content.welcome)
        while True:
            if not self.action():
                break
        print(CLI.content.farewell)
    @staticmethod
    def update_language(new_lang):
        CLI.language = new_lang
        CLI.content = Lang.content[CLI.language]
        CLI.make_commands()
    @staticmethod
    def change_lang():
        new_lang = input(Lang.prompt_with_current.format(CLI.content.cli.language.change_lang_prompt, CLI.language))
        if new_lang in Lang.content.keys():
            CLI.update_language(new_lang)
            print(CLI.content.cli.language.apply_lang)
        elif new_lang == "":
            print(CLI.content.cli.language.apply_lang)
        else:
            print(CLI.content.cli.language.change_failed)
            print(', '.join(Lang.content.keys()))
        return True
    def action(self):
        CLI.display_window(CLI.content.cli.hello, clear=False)
        i = 0
        for command in CLI.commands:
            for action, action_info in command.items():
                print("{}. {}".format(i, action))
                i += 1
        return self.do(self.dispatcher(input("({}): ".format(CLI.content.cli.action))))()
    def do(self, numb_action):
        if type(numb_action) is int:
            for command_info in CLI.commands[numb_action].values():
                return command_info['action']
        else:
            return CLI.Commands.not_exist()
    def dispatcher(self, action):
        numb_action = None
        try:
            numb_action = int(action)
        except ValueError:
            for i, command in enumerate(CLI.commands):
                for command_string in command.keys(): # only one
                    if utils.normalize_text(action) in utils.normalize_text(command_string):
                        numb_action = i
                        break
        return numb_action
if __name__ == '__main__':
    CLI()