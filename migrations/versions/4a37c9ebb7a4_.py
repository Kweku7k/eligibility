"""empty message

Revision ID: 4a37c9ebb7a4
Revises: 5877e6ad8c54
Create Date: 2021-10-06 18:01:11.589159

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a37c9ebb7a4'
down_revision = '5877e6ad8c54'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('course', sa.Column('tempField', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('course', 'tempField')
    # ### end Alembic commands ###
