"""empty message

Revision ID: 9b324e00578e
Revises: 718431f4fcda
Create Date: 2024-11-14 14:46:56.695384

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b324e00578e'
down_revision = '718431f4fcda'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Artist', schema=None) as batch_op:
        batch_op.add_column(sa.Column('website_link', sa.String(length=120), nullable=True))
        batch_op.add_column(sa.Column('seeking_venue', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('seeking_description', sa.String(length=120), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Artist', schema=None) as batch_op:
        batch_op.drop_column('seeking_description')
        batch_op.drop_column('seeking_venue')
        batch_op.drop_column('website_link')

    # ### end Alembic commands ###