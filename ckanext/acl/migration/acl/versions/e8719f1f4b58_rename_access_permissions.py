"""Rename access_permissions

Revision ID: e8719f1f4b58
Revises: 62270696e9e9
Create Date: 2020-07-09 20:03:35.095805

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "e8719f1f4b58"
down_revision = "62270696e9e9"
branch_labels = None
depends_on = None


def upgrade():
    op.rename_table("access_permissions", "acl_access_permissions")


def downgrade():
    op.rename_table("acl_access_permissions", "access_permissions")
