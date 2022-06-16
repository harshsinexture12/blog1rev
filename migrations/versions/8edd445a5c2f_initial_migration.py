"""Initial migration.

Revision ID: 8edd445a5c2f
Revises: 
Create Date: 2022-06-16 16:57:10.505948

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8edd445a5c2f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.String(length=200), nullable=False),
    sa.Column('password', sa.String(length=400), nullable=False),
    sa.Column('full_name', sa.String(length=100), nullable=False),
    sa.Column('user_pic', sa.String(length=255), nullable=True),
    sa.Column('about_author', sa.String(length=200), nullable=True),
    sa.Column('email', sa.String(length=200), nullable=False),
    sa.Column('is_admin', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('follower__request',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('follower_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['follower_id'], ['users.id'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('file', sa.String(length=512), nullable=True),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('date_posted', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment_msg', sa.String(length=512), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('date_posted', sa.DateTime(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('like',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('like')
    op.drop_table('comment')
    op.drop_table('post')
    op.drop_table('follower__request')
    op.drop_table('users')
    # ### end Alembic commands ###
