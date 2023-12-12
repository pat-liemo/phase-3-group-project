"""Database Creation

Revision ID: 2c1e26277ace
Revises: 467cb47fbf0c
Create Date: 2023-12-12 12:04:43.516126

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2c1e26277ace'
down_revision: Union[str, None] = '467cb47fbf0c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
