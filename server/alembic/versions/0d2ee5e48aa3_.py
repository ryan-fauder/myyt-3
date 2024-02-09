"""empty message

Revision ID: 0d2ee5e48aa3
Revises: bc458ebb3021
Create Date: 2024-02-09 10:40:31.365143

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0d2ee5e48aa3'
down_revision: Union[str, None] = 'bc458ebb3021'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('datanode', sa.Column('status', sa.Enum('Online', 'Offline', 'Busy'), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('datanode', 'status')
    # ### end Alembic commands ###
