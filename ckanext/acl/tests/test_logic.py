import pytest
from ckan.tests.helpers import call_action
from ckan.tests.factories import User

from ckanext.acl.access_permission import ACCESS_PERMISSIONS
import ckan.plugins.toolkit as toolkit


@pytest.fixture()
def base_permission():
    ACCESS_PERMISSIONS.clear()
    ACCESS_PERMISSIONS.create_permission("organization_create")


@pytest.mark.usefixtures("clean_db", "base_permission")
class TestLogic(object):
    def test_access_permission_show(self):
        user = User()

        with pytest.raises(toolkit.ValidationError):
            call_action("access_permission_show")

        perms = call_action("access_permission_show", id=user["id"])
        assert perms == {}

        call_action(
            "access_permission_set", username=user["name"], perm=["organization_create"]
        )

        perms = call_action("access_permission_show", id=user["id"])

        assert perms["owner_id"] == user["id"]
        assert perms["permissions"] == ["organization_create"]

    def test_check_access_with_perms(self):
        user = User()
        context = {"user": user["name"]}

        with pytest.raises(toolkit.NotAuthorized):
            toolkit.check_access("organization_create", context)

        call_action(
            "access_permission_set", username=user["name"], perm=["organization_create"]
        )

        acc = toolkit.check_access("organization_create", context)
        assert acc
