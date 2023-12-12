"""Creation of tables

Revision ID: 154fba6ea62b
Revises: 2c1e26277ace
Create Date: 2023-12-12 12:05:16.202138

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '154fba6ea62b'
down_revision: Union[str, None] = '2c1e26277ace'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("sneakers",
        sa.Column("id", sa.Integer(), nullable= False),        
        sa.Column("brand", sa.String(), nullable= False), 
        sa.Column("size", sa.Integer(), nullable= False), 
        sa.Column("colour", sa.String(), nullable= False),
        sa.Column("price", sa.Integer(), nullable= False),
        sa.Column("is_available", sa.Boolean(), default= True),

        sa.PrimaryKeyConstraint('id')
        )
    
    op.create_table("customers",
        sa.Column("id", sa.Integer(), nullable= False),        
        sa.Column("first_name", sa.String(), nullable= False), 
        sa.Column("last_name", sa.String(), nullable= False), 
        sa.Column("email", sa.String(), nullable= False),
        sa.Column("contact", sa.Integer(), nullable= False),

        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint("email")
        )
    
    op.create_table("reviews",
        sa.Column("id", sa.Integer(), nullable= False),        
        sa.Column("customer_id", sa.Integer(), nullable= False), 
        sa.Column("sneaker_id", sa.Integer(), nullable= False),
        sa.Column("rating", sa.Integer(), nullable= False),
        sa.Column("created_at", sa.DateTime(timezone=True), default= sa.func.now()), 

        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(["customer_id"], ["customers.id"]),
        sa.ForeignKeyConstraint(["sneaker_id"], ["sneakers.id"])
        )


def downgrade() -> None:
    pass
