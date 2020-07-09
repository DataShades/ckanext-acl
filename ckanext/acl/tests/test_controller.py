import pytest
from bs4 import BeautifulSoup

from ckan.tests.factories import Sysadmin
import ckan.plugins.toolkit as tk

from ckanext.acl.access_permission import ACCESS_PERMISSIONS


@pytest.mark.usefixtures("clean_db")
class TestACLController(object):
    def test_manage_permissions_page(self, app):

        url = tk.url_for("acl.manage_permissions")
        admin = Sysadmin()

        ACCESS_PERMISSIONS.clear()

        resp = app.get(
            url, extra_environ={"REMOTE_USER": admin["name"].encode("utf-8")}
        )
        page = BeautifulSoup(resp.body)
        checkboxes = page.select(".perm-checkbox input")
        pl = ACCESS_PERMISSIONS.permissions_list()

        assert pl == []
        assert pl == checkboxes

        test_perm_list = ["organization_create", "package_create"]
        for perm in test_perm_list:
            ACCESS_PERMISSIONS.create_permission(perm)

        resp = app.get(
            url, extra_environ={"REMOTE_USER": admin["name"].encode("utf-8")}
        )
        page = BeautifulSoup(resp.body)
        checkboxes = page.select(".perm-checkbox input")
        pl = ACCESS_PERMISSIONS.permissions_list()

        assert pl == test_perm_list
        assert len(pl) == len(checkboxes)
