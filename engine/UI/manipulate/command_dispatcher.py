import utils.utils as utils
def refresh(UI_class):
    return True
def dispatcher(Action_class, action):
    numb_action = None
    if action:
        try:
            numb_action = int(action)
        except ValueError:
            for i, command in enumerate(Action_class.commands):
                for command_string in command.keys():  # only one
                    if utils.normalize_text(action) in utils.normalize_text(command_string):
                        numb_action = i
                        return numb_action
    return numb_action

def do(Action_class, numb_action):
    if type(numb_action) is int:
        for command_info in Action_class.commands[numb_action].values():
            return command_info['action']
    elif not numb_action:
        return refresh
    else:
        return Action_class.Commands.not_exist()
