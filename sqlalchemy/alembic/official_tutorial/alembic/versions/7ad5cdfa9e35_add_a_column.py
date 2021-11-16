"""Add a column

Revision ID: 7ad5cdfa9e35
Revises: 50fed17f775d
Create Date: 2021-11-16 18:20:03.104487

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ad5cdfa9e35'
down_revision = '50fed17f775d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('account', sa.Column('last_transaction_date', sa.DateTime))

def downgrade():
    op.drop_column('account', 'last_transaction_date')

