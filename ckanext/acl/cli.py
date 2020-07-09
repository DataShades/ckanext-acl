# -*- coding: utf-8 -*-

import click


def get_commands():
    return [acl]


@click.group()
def acl():
    pass
