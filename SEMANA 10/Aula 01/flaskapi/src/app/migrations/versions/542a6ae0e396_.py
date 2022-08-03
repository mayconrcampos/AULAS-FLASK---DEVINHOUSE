"""empty message

Revision ID: 542a6ae0e396
Revises: 9c48653beea4
Create Date: 2022-08-02 21:37:05.570437

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '542a6ae0e396'
down_revision = '9c48653beea4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('developers', sa.Column('id_user', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'developers', 'users', ['id_user'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'developers', type_='foreignkey')
    op.drop_column('developers', 'id_user')
    # ### end Alembic commands ###
