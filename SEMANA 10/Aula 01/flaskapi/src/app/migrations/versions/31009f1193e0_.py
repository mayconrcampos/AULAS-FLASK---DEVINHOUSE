"""empty message

Revision ID: 31009f1193e0
Revises: 0134b0df7697
Create Date: 2022-08-02 21:08:54.279594

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31009f1193e0'
down_revision = '0134b0df7697'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('countrys',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('language', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('states',
    sa.Column('id', sa.Integer(), nullable=False, auto_increment=True),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('initials', sa.String(length=2), nullable=False),
    sa.Column('country_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['country_id'], ['countrys.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cities',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('id_state', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_state'], ['states.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cities')
    op.drop_table('states')
    op.drop_table('countrys')
    # ### end Alembic commands ###