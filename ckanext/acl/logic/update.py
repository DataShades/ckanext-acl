import ckan.plugins.toolkit as toolkit
import ckan.model as model
from ckanext.acl.access_permission import ACCESS_PERMISSIONS
from ckanext.acl.model.acl import AccessPermissions


def update_actions_dict():
    return {
        "access_permission_set": access_permission_set,
    }


def access_permission_set(context, data_dict):
    """
    Return access permissions of user.

    :param id: the id or name of the user
    :type id: string
    :rtype: dictionary
    """
    username, perm = toolkit.get_or_bust(data_dict, ["username", "perm"])
    toolkit.check_access("update_access_permission", context, data_dict)
    user = model.User.get(username)
    if user is None:
        raise toolkit.ValidationError("User not found")
    permissions = ACCESS_PERMISSIONS.get_user_permissions(user.id)
    if not permissions:
        permissions = AccessPermissions(owner_id=user.id)
        model.Session.add(permissions)
    permissions.set_permissions(perm)
    model.Session.commit()

    return permissions.as_dict()
