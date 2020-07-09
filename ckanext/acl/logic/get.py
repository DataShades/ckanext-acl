import ckan.plugins.toolkit as toolkit
import ckan.model as model
from ckanext.acl.access_permission import ACCESS_PERMISSIONS


def get_actions_dict():
    return {
        "access_permission_show": access_permission_show,
    }


@toolkit.side_effect_free
def access_permission_show(context, data_dict):
    """
    Return access permissions of user.

    :param id: the id or name of the user
    :type id: string
    :rtype: dictionary
    """
    model = context["model"]
    context["session"] = model.Session
    id = toolkit.get_or_bust(data_dict, "id")

    user = model.User.get(id)
    if user:
        perms = ACCESS_PERMISSIONS.get_user_permissions(user.id)
        if perms:
            return perms.as_dict()
        else:
            return {}
    raise toolkit.ObjectNotFound("User not found")
