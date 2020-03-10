"""empty message

Revision ID: d6232ab3b7e9
Revises: 
Create Date: 2020-03-10 19:39:05.100966

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6232ab3b7e9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('data_provider',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_data_provider_name'), 'data_provider', ['name'], unique=True)
    op.create_table('organisation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('data_storage_location',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data_provider_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('continent', sa.String(length=120), nullable=False),
    sa.Column('country', sa.String(length=120), nullable=False),
    sa.ForeignKeyConstraint(['data_provider_id'], ['data_provider.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_data_storage_location_continent'), 'data_storage_location', ['continent'], unique=False)
    op.create_index(op.f('ix_data_storage_location_country'), 'data_storage_location', ['country'], unique=False)
    op.create_index(op.f('ix_data_storage_location_name'), 'data_storage_location', ['name'], unique=False)
    op.create_table('digital_asset',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('organisation_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=1024), nullable=False),
    sa.Column('type', sa.String(length=1024), nullable=False),
    sa.ForeignKeyConstraint(['organisation_id'], ['organisation.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_digital_asset_name'), 'digital_asset', ['name'], unique=False)
    op.create_index(op.f('ix_digital_asset_type'), 'digital_asset', ['type'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('first_name', sa.String(length=120), nullable=False),
    sa.Column('last_name', sa.String(length=120), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.Column('organisation_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['organisation_id'], ['organisation.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('DigitalAssetStorage',
    sa.Column('asset_id', sa.Integer(), nullable=False),
    sa.Column('data_storage_location_id', sa.Integer(), nullable=False),
    sa.Column('uri', sa.String(length=1024), nullable=False),
    sa.ForeignKeyConstraint(['asset_id'], ['digital_asset.id'], ),
    sa.ForeignKeyConstraint(['data_storage_location_id'], ['data_storage_location.id'], ),
    sa.PrimaryKeyConstraint('asset_id', 'data_storage_location_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('DigitalAssetStorage')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_digital_asset_type'), table_name='digital_asset')
    op.drop_index(op.f('ix_digital_asset_name'), table_name='digital_asset')
    op.drop_table('digital_asset')
    op.drop_index(op.f('ix_data_storage_location_name'), table_name='data_storage_location')
    op.drop_index(op.f('ix_data_storage_location_country'), table_name='data_storage_location')
    op.drop_index(op.f('ix_data_storage_location_continent'), table_name='data_storage_location')
    op.drop_table('data_storage_location')
    op.drop_table('organisation')
    op.drop_index(op.f('ix_data_provider_name'), table_name='data_provider')
    op.drop_table('data_provider')
    # ### end Alembic commands ###
