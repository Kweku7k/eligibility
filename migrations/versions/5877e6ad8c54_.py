"""empty message

Revision ID: 5877e6ad8c54
Revises: 
Create Date: 2021-10-02 04:15:43.911917

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5877e6ad8c54'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('course', sa.Column('department', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('course', 'department')
    # ### end Alembic commands ###
