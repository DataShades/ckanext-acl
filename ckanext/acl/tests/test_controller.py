import nose.tools as nt
from ckan.tests.helpers import FunctionalTestBase, _get_test_app
from ckan.tests.factories import Sysadmin
from routes import url_for
from . import initdb
from ..access_permission import ACCESS_PERMISSIONS


class TestACLController(FunctionalTestBase):

    def setup(self):
        super(TestACLController, self).setup()
        initdb()

    def test_manage_permissions_page(self):
        app = _get_test_app()

        url = url_for('manage_permissions')
        admin = Sysadmin()

        ACCESS_PERMISSIONS.clear()

        page = app.get(url, extra_environ={'REMOTE_USER': admin['name'].encode('utf-8')})
        checkboxes = page.html.select('.perm-checkbox input')
        pl = ACCESS_PERMISSIONS.permissions_list()

        nt.assert_equal(pl, [])
        nt.assert_equal(pl, checkboxes)

        test_perm_list = ['organization_create', 'package_create']
        for perm in test_perm_list:
            ACCESS_PERMISSIONS.create_permission(perm)

        page = app.get(url, extra_environ={'REMOTE_USER': admin['name'].encode('utf-8')})
        checkboxes = page.html.select('.perm-checkbox input')
        pl = ACCESS_PERMISSIONS.permissions_list()

        nt.assert_equal(pl, test_perm_list)
        nt.assert_equal(len(pl), len(checkboxes))
