"""create account table

Revision ID: 50fed17f775d
Revises: 
Create Date: 2021-11-16 18:09:42.274095

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50fed17f775d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'account',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
    )

def downgrade():
    op.drop_table('account')