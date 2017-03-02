import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from routes.mapper import SubMapper
import ckanext.acl.logic as acl_logic
import ckanext.acl.logic.auth as acl_auth
from .interfaces import IACL
from . import ORGANIZATION_CREATE, USER_DELETE
from .access_permission import ACCESS_PERMISSIONS


class AclPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IRoutes, inherit=True)
    plugins.implements(plugins.IActions)
    plugins.implements(IACL)
    plugins.implements(plugins.IConfigurable)
    plugins.implements(plugins.IAuthFunctions)

    # IAuthFunctions

    def get_auth_functions(self):
        return acl_auth.get_auth_functions()

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'acl')
        if toolkit.check_ckan_version(min_version='2.4'):
            toolkit.add_ckan_admin_tab(config_, 'manage_permissions', 'Permissions')

    # IConfigurable

    def configure(self, config_):
        for item in plugins.PluginImplementations(IACL):
            item.update_permission_list(ACCESS_PERMISSIONS)
        ACCESS_PERMISSIONS.decorate_original()

    # IRoutes

    def before_map(self, map):
        with SubMapper(map, controller='ckanext.acl.controller:ACLController') as m:
            m.connect('manage_permissions', '/ckan-admin/manage-permissions',
                      action='manage_permissions', ckan_icon="unlock-alt")
        return map

    # IActions

    def get_actions(self):
        """Return new api actions."""
        actions = acl_logic.get_actions()
        return actions

    # IACL

    def update_permission_list(self, perms):
        perms.create_permission(ORGANIZATION_CREATE)
        perms.create_permission(USER_DELETE)
