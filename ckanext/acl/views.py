# -*- coding: utf-8 -*-

import logging
from flask import Blueprint

import ckan.model as model
import ckan.plugins.toolkit as tk
import ckan.logic as logic
from ckanext.acl.access_permission import ACCESS_PERMISSIONS

log = logging.getLogger(__name__)
acl = Blueprint("acl", __name__)


def get_blueprints():
    return [acl]


@acl.route("/ckan-admin/manage-permissions", methods=("GET", "POST"))
def manage_permissions():

    context = {"model": model, "user": tk.c.user, "auth_user_obj": tk.c.userobj}
    try:
        logic.check_access("sysadmin", context, {})
    except logic.NotAuthorized:
        code, msg = 401, "Not authorized to see this page"
        tk.abort(code, tk._(msg))

    username = tk.request.args.get("username", "")
    data = tk.request.form
    if "save" in data:
        new_perm = data.getall("perm")
        username = data.get("username")
        data_dict = {"username": username, "perm": new_perm}
        try:
            tk.get_action("access_permission_set")(context, data_dict)

        except tk.ValidationError as e:
            log.error(e)
        return tk.redirect_to(tk.h.url_for("acl.manage_permissions", username=username))
    extra_vars = {"perm_list": ACCESS_PERMISSIONS, "username": username}
    return tk.render("admin/manage_permissions.html", extra_vars)
