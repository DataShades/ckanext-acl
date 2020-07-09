
=============
ckanext-acl
=============

.. Put a description of your extension here:
   What does it do? What features does it have?
   Consider including some screenshots or embedding a video!


Implentation of ACL for ckan.

When extension enabled, new tab `Permissions` added to admin interface.
Here you can manage user permissions on per-user level.

In order to add new managed permission, one should implement ``ckanext.acl.interfaces.IACL``
and define ``update_permission_list`` method in plugin and change ``perm`` - first positional argument
passed into this method. ``perms`` is ``ckanext.acl.access_permissions.AccessPermissions`` object so
you can check available actions there.

Example of code that you can use in your plugin(will allow any user to create new organization)::
  from ckanext.acl.interfaces import IACL

  plugins.implements(IACL)

  # IACL

  def update_permission_list(self, perms):
      perms.create_permission('organization_create')
