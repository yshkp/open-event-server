"""empty message

Revision ID: 163f9fc56815
Revises: 000b9376b87b
Create Date: 2018-07-07 20:02:58.671894

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '163f9fc56815'
down_revision = '000b9376b87b'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('message_settings', sa.Column('sent_at', sa.DateTime(timezone=True), nullable=True))
    op.execute(
        "ALTER TABLE message_settings ALTER COLUMN mail_status TYPE BOOLEAN "
        "USING mail_status::boolean")
    op.execute(
        "ALTER TABLE message_settings ALTER COLUMN notification_status "
        "TYPE BOOLEAN USING notification_status::boolean")
    op.execute(
        "ALTER TABLE message_settings ALTER COLUMN user_control_status "
        "TYPE BOOLEAN USING user_control_status::boolean")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('message_settings', 'user_control_status',
               existing_type=sa.Boolean(),
               type_=sa.INTEGER(),
               existing_nullable=True)
    op.alter_column('message_settings', 'notification_status',
               existing_type=sa.Boolean(),
               type_=sa.INTEGER(),
               existing_nullable=True)
    op.alter_column('message_settings', 'mail_status',
               existing_type=sa.Boolean(),
               type_=sa.INTEGER(),
               existing_nullable=True)
    op.drop_column('message_settings', 'sent_at')
    # ### end Alembic commands ###
