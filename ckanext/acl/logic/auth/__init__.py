from .update import update_auth_dict


def get_auth_functions():
    auth = {}

    auth.update(update_auth_dict())

    return auth
