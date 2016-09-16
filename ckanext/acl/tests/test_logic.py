import nose.tools as nt
from ckan.tests.helpers import FunctionalTestBase, call_action
from ckan.tests.factories import User
from . import initdb
from ..access_permission import ACCESS_PERMISSIONS
import ckan.plugins.toolkit as toolkit


class TestLogic(FunctionalTestBase):

    def setup(self):
        super(TestLogic, self).setup()
        initdb()

        ACCESS_PERMISSIONS.clear()
        ACCESS_PERMISSIONS.create_permission('organization_create')

    def test_access_permission_show(self):

        user = User()

        nt.assert_raises(
            toolkit.ValidationError, call_action,
            'access_permission_show'
        )

        perms = call_action('access_permission_show', id=user['id'])
        nt.assert_equal({}, perms)

        call_action('access_permission_set', username=user['name'], perm=['organization_create'])

        perms = call_action('access_permission_show', id=user['id'])

        nt.assert_equal(perms['owner_id'], user['id'])
        nt.assert_equal(perms['permissions'], ['organization_create'])

    def test_check_access_with_perms(self):
        user = User()
        context = {'user': user['name']}

        nt.assert_raises(
            toolkit.NotAuthorized,
            toolkit.check_access,
            'organization_create',
            context
        )

        call_action('access_permission_set', username=user['name'], perm=['organization_create'])

        acc = toolkit.check_access('organization_create', context)
        nt.assert_true(acc)
