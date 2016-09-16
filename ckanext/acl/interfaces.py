from ckan.plugins.interfaces import Interface


class IACL(Interface):
    """
    Hook into ACL extension
    """

    def update_permission_list(self, perms):
        return perms
