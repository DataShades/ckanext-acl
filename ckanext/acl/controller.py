import ckan.lib.base as base
import ckan.model as model
import ckan.plugins.toolkit as toolkit
import ckan.logic as logic
from ckan.common import _
from ckanext.acl.access_permission import ACCESS_PERMISSIONS
from ckanext.acl.model.acl import AccessPermissions
import ckan.lib.helpers as h
import logging
log = logging.getLogger(__name__)


class ACLController(base.BaseController):

    def manage_permissions(self):
        """Admin page."""
        context = {'model': model,
                   'user': toolkit.c.user,
                   'auth_user_obj': toolkit.c.userobj}
        try:
            logic.check_access('sysadmin', context, {})
        except logic.NotAuthorized:
            code, msg = 401, 'Not authorized to see this page'
            base.abort(code, toolkit._(msg))

        username = toolkit.request.GET.get('username', '')
        data = toolkit.request.POST
        if 'save' in data:
            new_perm = data.getall('perm')
            username = data.get('username')
            data_dict = {
                'username': username,
                'perm': new_perm
            }
            try:
                toolkit.get_action('access_permission_set')(context, data_dict)

            except toolkit.ValidationError as e:
                log.error(e)
            return base.redirect(h.url_for('manage_permissions', username=username))
        vars = {'perm_list': ACCESS_PERMISSIONS, 'username': username}
        return base.render('admin/manage_permissions.html',
                           extra_vars=vars)
