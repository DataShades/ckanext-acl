import ckan.plugins.toolkit as toolkit


def update_auth_dict():
    return {
        "update_access_permission": update_access_permission,
    }


def update_access_permission(context, data_dict):
    return toolkit.check_access("sysadmin", context, data_dict)
