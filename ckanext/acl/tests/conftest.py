# -*- coding: utf-8 -*-
import pytest
from ckan.cli.cli import ckan


@pytest.fixture()
def clean_db(reset_db, cli):
    reset_db()
    cli.invoke(ckan, ["db", "upgrade", "-p", "acl"])
