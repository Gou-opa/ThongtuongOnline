from engine.UI.manipulate.command_dispatcher import dispatcher, do
from os import system, name
from engine.lang import Lang


class Windows:
    commands = None

    class Commands:
        @staticmethod
        def exit(UI_class):
            return False
        @staticmethod
        def not_exist(UI_class):
            print(UI_class.content.window.not_exist)
            return True
    def action(UI_class, Action_class):
        Windows.header(UI_class.content.window.action, clear=False)
        i = 0
        for command in Action_class.commands:
            for action, action_info in command.items():
                print("{}. {}".format(i, action))
                i += 1
        return do(Action_class, dispatcher(Action_class, input("({}): ".format(UI_class.content.window.action))))(
            UI_class)
    @staticmethod
    def clear():
        if name == 'nt':  # for windows
            _ = system('cls')
        else:  # for mac and linux(here, os.name is 'posix')
            _ = system('clear')
    @classmethod
    def header(_class_, window_hello, clear=True):
        if clear:
            _class_.clear()
        print(Lang.hello.format(window_hello))
        print(Lang.line_break)
    @classmethod
    def display_windows(_class_, UI_class, *args, **kwargs):
        if not UI_class:
            UI_class = _class_
        exitcode = 0
        window_obj = _class_(UI_class, *args, **kwargs)
        while not exitcode:
            exitcode = window_obj.display()
        return True



    @classmethod
    def make_hello_and_commands(_class_, UI_class): # override: define
        _class_.hello = ""
        _class_.commands = []
    @classmethod
    def windows_commands(_class_, UI_class):
        basic_commands = [
            {UI_class.content.help.command:
                {
                    "desc": UI_class.content.help.desc,
                    "action": Help.display_windows
                }
            },
            {UI_class.content.setting.command:
                {
                    "desc": UI_class.content.setting.desc,
                    "action": Setting.display_windows
                }
            },
            {UI_class.content.window.exit_command:
                {
                    "desc": UI_class.content.window.exit_desc,
                    "action": Windows.Commands.exit
                }
            }
        ]
        if _class_.commands:
            rm = []
            for command in _class_.commands:
                if command in basic_commands:
                    rm.append(command)
            for command in rm:
                _class_.commands.remove(command)
            _class_.commands = basic_commands[:1] + _class_.commands + basic_commands[1:]
        else:
            _class_.commands = basic_commands


    def __init__(self, UI_class):
        self.onload()
        self.__class__.make_hello_and_commands(UI_class)
        self.__class__.windows_commands(UI_class)
        self.UI = UI_class
        self.content = UI_class.content

    def windows_action(self):
        pass
    def display(self):
        self.onready()
        while True:
            Windows.header(self.__class__.hello)
            self.windows_action()
            if not Windows.action(self.UI, self.__class__):
                self.onexit()
                return True
    def onready(self):
        pass
    def onload(self):
        pass
    def onexit(self):
        pass
    def remove_current_window_action_in_command(self,action):
        rm = None
        for command in self.__class__.commands:
            if list(command.keys())[0] == action:
                rm = command
                break
        self.__class__.commands.remove(rm)
class Setting(Windows):
    @classmethod
    def make_hello_and_commands(_class_, UI_class):
        _class_.hello = UI_class.content.setting.hello
        _class_.commands = [
            {UI_class.content.language.command:
                {
                    "desc": UI_class.content.language.desc,
                    "action": UI_class.Commands.change_lang
                }
            }
        ]
    def onready(self):
        self.remove_current_window_action_in_command(self.content.setting.command)
class Help(Windows):
    @classmethod
    def make_hello_and_commands(_class_, UI_class):
        _class_.hello = UI_class.content.help.hello
    def onready(self):
        self.remove_current_window_action_in_command(self.content.help.command)
    def windows_action(self):
        Windows.header(self.content.help.hello)
        i = 0
        for command in self.__class__.commands:
            for action, command_info in command.items():
                print("{}. {}: {}".format(i, action, command_info['desc']))
                i += 1
        return True