from .get import get_actions_dict
from .update import update_actions_dict


def get_actions():
    actions = {}
    actions.update(get_actions_dict())
    actions.update(update_actions_dict())

    return actions
