"""empty message

Revision ID: 0134b0df7697
Revises: 51c54f9cbfd4
Create Date: 2022-08-02 20:19:25.537924

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0134b0df7697'
down_revision = '51c54f9cbfd4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('developers',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('months_experience', sa.Integer(), nullable=False),
    sa.Column('accepted_remote_work', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('developers')
    # ### end Alembic commands ###
