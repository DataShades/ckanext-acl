import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import ckanext.acl.logic as acl_logic
import ckanext.acl.logic.auth as acl_auth
import ckanext.acl.views as views
import ckanext.acl.cli as cli
from .interfaces import IACL
from . import ORGANIZATION_CREATE
from .access_permission import ACCESS_PERMISSIONS


class AclPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IBlueprint)
    plugins.implements(plugins.IActions)
    plugins.implements(IACL)
    plugins.implements(plugins.IConfigurable)
    plugins.implements(plugins.IAuthFunctions)
    plugins.implements(plugins.IClick)

    # IClick

    def get_commands(self):
        return cli.get_commands()

    # IAuthFunctions

    def get_auth_functions(self):
        return acl_auth.get_auth_functions()

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, "templates")
        toolkit.add_public_directory(config_, "public")
        toolkit.add_resource("assets", "acl")
        toolkit.add_ckan_admin_tab(config_, "acl.manage_permissions", "Permissions")

    # IConfigurable

    def configure(self, config_):
        for item in plugins.PluginImplementations(IACL):
            item.update_permission_list(ACCESS_PERMISSIONS)
        ACCESS_PERMISSIONS.decorate_original()

    # IBluepring

    def get_blueprint(self):
        return views.get_blueprints()

    # IActions

    def get_actions(self):
        """Return new api actions."""
        actions = acl_logic.get_actions()
        return actions

    # IACL

    def update_permission_list(self, perms):
        perms.create_permission(ORGANIZATION_CREATE)
