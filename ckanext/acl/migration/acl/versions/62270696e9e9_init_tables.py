"""Init tables

Revision ID: 62270696e9e9
Revises:
Create Date: 2020-07-09 19:43:11.106368

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector
import sqlalchemy.dialects.postgresql as postgresql

# revision identifiers, used by Alembic.
revision = "62270696e9e9"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)
    tables = inspector.get_table_names()
    if "access_permissions" in tables:
        return
    op.create_table(
        "access_permissions",
        sa.Column("owner_id", sa.UnicodeText, nullable=False, primary_key=True),
        sa.Column("permissions", postgresql.ARRAY(sa.UnicodeText), nullable=False),
    )


def downgrade():
    op.drop_table("access_permissions")
