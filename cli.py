# -*- coding: utf-8 -*-
from engine.UI.CLI.windows import Windows
from engine.UI.CLI.welcome import Welcome
from engine.lang import Lang

class CLI:
    language = None
    content = None
    class Commands:
        @staticmethod
        def change_lang(UI_class):
            Windows.header(UI_class.content.language.hello)
            new_lang = input(Lang.prompt_with_current.format(UI_class.content.language.change_lang_prompt, UI_class.language))
            if new_lang in Lang.content.keys():
                UI_class.update_language(new_lang)
                print(UI_class.content.language.apply_lang)
            elif new_lang == "":
                print(UI_class.content.language.apply_lang)
            else:
                print(UI_class.content.language.change_failed)
                print(', '.join(Lang.content.keys()))
            return True

    @staticmethod
    def update_language(new_lang):
        CLI.language = new_lang
        CLI.content = Lang.content[CLI.language]
    def __init__(self):
        self.update_language('vi')
        self.display_welcome()
    def display_welcome(self):
        exitcode = 0
        window_obj = Welcome(UI_class=CLI)
        while not exitcode:
            exitcode = window_obj.display()

if __name__ == '__main__':
    CLI()