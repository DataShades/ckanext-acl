from ckan.model import Session
from .model.acl import AccessPermissions as APModel

try:
    import ckan.authz as autz
except ImportError:
    import ckan.new_authz as autz
from functools import wraps
import logging

log = logging.getLogger(__name__)


def acl_available(func):
    func.acl_registered = True

    @wraps(func)
    def acl_wrapper(context, data_dict=None):
        try:
            user = context["auth_user_obj"]

            u_perm = ACCESS_PERMISSIONS.get_user_permissions(user.id)
            if u_perm and u_perm.has_permission(func.__name__):
                return {"success": True}
        except Exception as e:
            log.error("{0}: {1}".format(type(e), e))

        return func(context, data_dict)

    return acl_wrapper


class AccessPermissions:
    """Implementation of access permissions in CKAN."""

    def __init__(self):
        self._available_permissions = []

    def permissions_list(self):
        """Show all available permissions."""
        return self._available_permissions

    def permission_exists(self, permission):
        """Check whether list of permissions contains this permission."""
        return permission in self._available_permissions

    def create_permission(self, permission):
        """Add permission to list."""
        if permission not in self._available_permissions:
            self._available_permissions.append(permission)
        return self

    def destroy_permission(self, permission):
        """Remove permission from list."""
        if permission in self._available_permissions:
            self._available_permissions.remove(permission)
        return self

    def get_user_permissions(self, id):
        """Get object with user's permissions."""
        permissions = Session.query(APModel).get(id)
        return permissions

    def humanize_permission(self, perm):
        """Convert permission's name to title format."""
        return perm.replace("_", " ").title()

    def clear(self):
        self._available_permissions = []

    def decorate_original(self):
        _a = autz._AuthFunctions
        original_get = _a.get

        @wraps(_a.get)
        def _get(function):
            func = original_get(function)

            if self.permission_exists(function):
                return acl_available(func)
            return func

        _a.get = _get


ACCESS_PERMISSIONS = AccessPermissions()
