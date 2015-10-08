"""Initial Plorma version.

Revision ID: 49d74299025
Revises: None
Create Date: 2015-10-08 14:54:43.332000

"""

# revision identifiers, used by Alembic.
revision = '49d74299025'
down_revision = None

from alembic import op
import sqlalchemy as sa


INSERTS = """
INSERT INTO usergroups (uuid, id, name, description, uid, gid) VALUES ('a81fc589dbb14afaaf731e25f78a560e', 1, 'admins', '', NULL, NULL);
INSERT INTO usergroups (uuid, id, name, description, uid, gid) VALUES ('25311fc258524725b34da917094a0292', 2, 'users', '', NULL, NULL);
INSERT INTO usergroups (uuid, id, name, description, uid, gid) VALUES ('ec58cd9c18804e65bea881f75cb54d36', 3, 'admin', '', NULL, NULL);
INSERT INTO modules (uuid, id, name, clazzpath, label, label_plural, description, str_repr, display, default_gid) VALUES ('d1763c385bd64d7185ca7fba9b3de845', 1, 'modules', 'ringo.model.modul.ModulItem', 'Modul', 'Modules', '', '%s|name', 'admin-menu', NULL);
INSERT INTO modules (uuid, id, name, clazzpath, label, label_plural, description, str_repr, display, default_gid) VALUES ('fcb3f8f87cc340358e18c4017bf93f34', 2, 'actions', 'ringo.model.modul.ActionItem', 'Action', 'Actions', '', '%s (%s/%s)|name,modul,url', 'hidden', NULL);
INSERT INTO modules (uuid, id, name, clazzpath, label, label_plural, description, str_repr, display, default_gid) VALUES ('74af1cfbf3de4bceb5f2cb483381229e', 4, 'usergroups', 'ringo.model.user.Usergroup', 'Usergroup', 'Usergroups', '', '%s|name', 'admin-menu', NULL);
INSERT INTO modules (uuid, id, name, clazzpath, label, label_plural, description, str_repr, display, default_gid) VALUES ('c0138448b3964a5682411f57409e67f1', 5, 'roles', 'ringo.model.user.Role', 'Role', 'Roles', '', '%s|name', 'admin-menu', NULL);
INSERT INTO modules (uuid, id, name, clazzpath, label, label_plural, description, str_repr, display, default_gid) VALUES ('7d99e6702cdc4a9c928c1eaa470e11b6', 6, 'profiles', 'ringo.model.user.Profile', 'Profile', 'Profiles', '', '%s %s|first_name,last_name', 'admin-menu', NULL);
INSERT INTO modules (uuid, id, name, clazzpath, label, label_plural, description, str_repr, display, default_gid) VALUES ('f5108e1ce27b4f229655d0ad35e843cb', 14, 'forms', 'ringo.model.form.Form', 'Form', 'Forms', '', '%s|title', 'admin-menu', NULL);
INSERT INTO modules (uuid, id, name, clazzpath, label, label_plural, description, str_repr, display, default_gid) VALUES ('9e6050dec2ab11e4906f0019e084be15', 1000, 'tasks', 'plorma.model.task.Task', 'Task', 'Tasks', '', '%s|name', 'header-menu', 2);
INSERT INTO modules (uuid, id, name, clazzpath, label, label_plural, description, str_repr, display, default_gid) VALUES ('7e5bbba9cd7f428aa2e063d1fcfb0eea', 1002, 'tags', 'ringo_tag.model.Tag', 'Tag', 'Tags', '', '%s|name', 'admin-menu', 2);
INSERT INTO modules (uuid, id, name, clazzpath, label, label_plural, description, str_repr, display, default_gid) VALUES ('7ef78644682b4cc285df1661d2fa7437', 1001, 'comments', 'ringo_comment.model.Comment', 'Comments', 'Comment', '', '%s|id', 'admin-menu', 2);
INSERT INTO modules (uuid, id, name, clazzpath, label, label_plural, description, str_repr, display, default_gid) VALUES ('70f24f2a8b63420e9afde6af43be45d2', 3, 'users', 'ringo.model.user.User', 'User', 'Users', '', '%s|login', 'admin-menu', 2);
INSERT INTO modules (uuid, id, name, clazzpath, label, label_plural, description, str_repr, display, default_gid) VALUES ('be7a2ab2e77e4f659ba646c8f757fe16', 1003, 'sprints', 'plorma.model.sprint.Sprint', 'Sprint', 'Sprints', '', '%s (%s - %s)|title,start,end', 'header-menu', NULL);
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('f175f1eba7b64ea7bdca22ba12f5e39d', 1, 1, 'List', 'list', 'icon-list-alt', '', false, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('4088d4e90ae845f197abfa1108c061ff', 2, 1, 'Read', 'read/{id}', 'icon-eye-open', '', false, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('be74bde114e84e1e8dbb5f3c3854a949', 3, 1, 'Update', 'update/{id}', 'icon-edit', '', false, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('587e8a890236458bb5e4e0dd7eb6849d', 4, 3, 'List', 'list', 'icon-list-alt', '', false, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('d3a18879564349b1bc879c837dc90041', 5, 3, 'Create', 'create', ' icon-plus', '', false, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('c698f6b9c804471e8b0b17369d9204a7', 6, 3, 'Read', 'read/{id}', 'icon-eye-open', '', false, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('ad3faf57c65b4daab99dfa4cb4118fda', 7, 3, 'Update', 'update/{id}', 'icon-edit', '', false, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('6f8ce37aa0924bf3b52c5570d3352e95', 8, 3, 'Delete', 'delete/{id}', 'icon-trash', '', true, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('47e6e02d0bc246699d92aea4c2f90b92', 9, 4, 'List', 'list', 'icon-list-alt', '', false, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('7de6e75399ae4794a03b61bac36afbbf', 10, 4, 'Create', 'create', ' icon-plus', '', false, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('8f2b1c32206949ac9cef4c660f0c9c6b', 11, 4, 'Read', 'read/{id}', 'icon-eye-open', '', false, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('50378069e10a4c9fb744fc76e3ba9338', 12, 4, 'Update', 'update/{id}', 'icon-edit', '', false, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('1c624bfaa39e4a35b07ee6132fa9ebf6', 13, 4, 'Delete', 'delete/{id}', 'icon-trash', '', true, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('a10159f5b92d40a1b0890cbcaf609795', 14, 5, 'List', 'list', 'icon-list-alt', '', false, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('adfb73a7fbe84d0584189def749b0827', 15, 5, 'Create', 'create', ' icon-plus', '', false, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('1ecfa4204afc450c96881816daac76e2', 16, 5, 'Read', 'read/{id}', 'icon-eye-open', '', false, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('c339166e8c694d20b737f902def31b24', 17, 5, 'Update', 'update/{id}', 'icon-edit', '', false, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('ecd2cc31240e48c287d63091aa2ee0e3', 18, 5, 'Delete', 'delete/{id}', 'icon-trash', '', true, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('a8e477e97a5744eb81544e9831e43905', 19, 6, 'List', 'list', 'icon-list-alt', '', false, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('0ada859b88c8400698ffe6530e7a5fa1', 20, 6, 'Read', 'read/{id}', 'icon-eye-open', '', false, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('97123f8eedff4d2ab5a624e40d6c0b9c', 21, 6, 'Update', 'update/{id}', 'icon-edit', '', false, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('f134e1c6b7ac416ebead7f9e8d56f84f', 63, 2, 'Export', 'export/{id}', 'icon-export', '', true, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('049b20d7af3c4fee95de03cc5299838d', 64, 2, 'Import', 'import', 'icon-import', '', false, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('26409b5b4c5541bfb9681ba8da2d6183', 65, 3, 'Export', 'export/{id}', 'icon-export', '', true, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('b5133cddb90a4b49b9915b94588e4755', 66, 3, 'Import', 'import', 'icon-import', '', false, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('fae37a0b9a9549cd9f8588e6c762b834', 67, 4, 'Export', 'export/{id}', 'icon-export', '', true, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('328ad0e3cce8430091123362e8c274d9', 68, 4, 'Import', 'import', 'icon-import', '', false, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('d0cf5aad0b864735936c23bfd4cdda88', 69, 5, 'Export', 'export/{id}', 'icon-export', '', true, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('39a3c12e4995451fad3507be9b97c96f', 70, 5, 'Import', 'import', 'icon-import', '', false, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('3fd988e79e8f45fda4883cb276f18d84', 89, 14, 'List', 'list', 'icon-list-alt', '', false, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('92753e993275495b83723ae2c3916e7d', 90, 14, 'Create', 'create', ' icon-plus', '', false, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('926fceba13404d31b9b9a6ccc4f1ef01', 91, 14, 'Read', 'read/{id}', 'icon-eye-open', '', false, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('7df85ce43e324840ac658e7c8582b553', 92, 14, 'Update', 'update/{id}', 'icon-edit', '', false, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('9a61ef9af8384f06a2a92c8a95abb830', 93, 14, 'Delete', 'delete/{id}', 'icon-trash', '', true, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('dc2d60b3d9324183954e8ea176e51e48', 94, 14, 'Import', 'import', 'icon-import', '', false, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('2be9665855ab43eb8bcbd74386254b18', 95, 14, 'Export', 'export/{id}', 'icon-export', '', true, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('d4e0e8c53c2841e98eda1efd800306fb', 104, 6, 'Export', 'export/{id}', 'icon-export', '', true, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('6bc3be84449643989996632f46ab27fa', 105, 6, 'Import', 'import', 'icon-import', '', false, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('84bda1cac2ad11e4906f0019e084be15', 106, 1000, 'List', 'list', 'icon-list-alt', '', false, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('0d63e866c2b011e4906f0019e084be15', 107, 1000, 'Create', 'create', 'icon-plus', '', false, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('a43d4baec2ad11e4906f0019e084be15', 108, 1000, 'Read', 'read/{id}', 'icon-eye-open', '', false, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('aafa42b2c2ad11e4906f0019e084be15', 109, 1000, 'Update', 'update/{id}', 'icon-pencil', '', false, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('acb05608c2af11e4906f0019e084be15', 110, 1000, 'Delete', 'delete/{id}', 'icon-trash', '', true, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('5719c46ec2ae11e4906f0019e084be15', 111, 1000, 'Import', 'import', 'icon-import', '', false, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('64551f02c2ae11e4906f0019e084be15', 112, 1000, 'Export', 'export/{id}', 'icon-export', '', true, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('0f217a9244c34fea82766811608e5214', 113, 1001, 'Read', 'read/{id}', 'icon-eye-open', '', false, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('cf42a76a6d954ad5ba371a512b9b0ce8', 114, 1001, 'Create', 'create', ' icon-plus', '', false, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('f470394f18c541369b115ac4ee38d058', 115, 1001, 'List', 'list', 'icon-list-alt', '', false, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('0bc7caae5ddb457aac35cebe3c50cc06', 116, 1001, 'Update', 'update/{id}', 'icon-edit', '', false, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('97244efda0fb413aa2cfded88dcad0c2', 117, 1001, 'Delete', 'delete/{id}', 'icon-trash', '', true, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('ed5cc4513977489d8e178aaa3bc28c73', 118, 1002, 'Read', 'read/{id}', 'icon-eye-open', '', false, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('74f0d8968f264afcad2311727f3b3ff5', 119, 1002, 'Create', 'create', ' icon-plus', '', false, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('f22027be18454fa79fa8d1c1bac3fedc', 120, 1002, 'List', 'list', 'icon-list-alt', '', false, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('f4ea931641b844baba80a9a27da45b8d', 121, 1002, 'Update', 'update/{id}', 'icon-edit', '', false, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('847e31fab7d1488d818b92ae52a8230e', 122, 1002, 'Delete', 'delete/{id}', 'icon-trash', '', true, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('72706145cfff40598a955e2519ba562c', 123, 1003, 'List', 'list', 'icon-list-alt', '', false, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('14f25990b05b49b4859daed89f175473', 124, 1003, 'Create', 'create', 'icon-plus', '', false, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('ac0be17f6e0d47289366af984346fc1c', 125, 1003, 'Read', 'read/{id}', 'icon-eye-open', '', false, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('4e23dd95289f4be6a4c78ae71c5c3bb2', 126, 1003, 'Update', 'update/{id}', 'icon-edit', '', false, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('05ea9cce36584311b9813a8ee0b18ad0', 127, 1003, 'Delete', 'delete/{id}', 'icon-eye-delete', '', false, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('ea98c7df93354613853db67a31ae10cc', 128, 1003, 'Import', 'import', 'icon-import', '', false, 'primary', '');
INSERT INTO actions (uuid, id, mid, name, url, icon, description, bundle, display, permission) VALUES ('ae133a9065564da6bda2643375bb35ae', 129, 1003, 'Export', 'export/{id}', 'icon-export', '', true, 'primary', '');
INSERT INTO user_settings (id, settings) VALUES (1, '{}');
INSERT INTO users (uuid, id, login, password, activated, activation_token, default_gid, sid, last_login, uid, gid) VALUES ('8ea901bc958340138c7ff7ef1c1f5637', 1, 'admin', '$pbkdf2-sha256$8392$ca5Vau09B2AMQWit1ZoTgg$yD/W9MpiDc17pA1vMNHH4jkk3DgGEd4W60zqlzR0.Ho', true, '', 3, 1, NULL, NULL, NULL);
INSERT INTO roles (uuid, id, label, name, description, admin, uid, gid) VALUES ('abbfbcabd04344c1983ba628baea6fde', 2, 'Users', 'user', '', false, NULL, NULL);
INSERT INTO roles (uuid, id, label, name, description, admin, uid, gid) VALUES ('e9dd93b904eb48cf88a6f86a9dd663b9', 3, 'Developer', 'developer', '', false, NULL, NULL);
INSERT INTO roles (uuid, id, label, name, description, admin, uid, gid) VALUES ('971aaa79dd6b4b3b93bb7d811f06d910', 4, 'Product Owner', 'productowner', '', false, NULL, NULL);
INSERT INTO roles (uuid, id, label, name, description, admin, uid, gid) VALUES ('38db659bde2843c6b3a052010d40c633', 1, 'Administration', 'admin', '', true, NULL, NULL);
INSERT INTO nm_action_roles (aid, rid) VALUES (20, 2);
INSERT INTO nm_action_roles (aid, rid) VALUES (21, 2);
INSERT INTO nm_action_roles (aid, rid) VALUES (106, 3);
INSERT INTO nm_action_roles (aid, rid) VALUES (107, 3);
INSERT INTO nm_action_roles (aid, rid) VALUES (108, 3);
INSERT INTO nm_action_roles (aid, rid) VALUES (109, 3);
INSERT INTO nm_action_roles (aid, rid) VALUES (110, 3);
INSERT INTO nm_action_roles (aid, rid) VALUES (111, 3);
INSERT INTO nm_action_roles (aid, rid) VALUES (112, 3);
INSERT INTO nm_action_roles (aid, rid) VALUES (113, 3);
INSERT INTO nm_action_roles (aid, rid) VALUES (114, 3);
INSERT INTO nm_action_roles (aid, rid) VALUES (115, 3);
INSERT INTO nm_action_roles (aid, rid) VALUES (116, 3);
INSERT INTO nm_action_roles (aid, rid) VALUES (117, 3);
INSERT INTO nm_action_roles (aid, rid) VALUES (118, 3);
INSERT INTO nm_action_roles (aid, rid) VALUES (120, 3);
INSERT INTO nm_action_roles (aid, rid) VALUES (123, 3);
INSERT INTO nm_action_roles (aid, rid) VALUES (125, 3);
INSERT INTO nm_action_roles (aid, rid) VALUES (119, 4);
INSERT INTO nm_action_roles (aid, rid) VALUES (121, 4);
INSERT INTO nm_action_roles (aid, rid) VALUES (122, 4);
INSERT INTO nm_action_roles (aid, rid) VALUES (124, 4);
INSERT INTO nm_action_roles (aid, rid) VALUES (126, 4);
INSERT INTO nm_action_roles (aid, rid) VALUES (127, 4);
INSERT INTO nm_action_roles (aid, rid) VALUES (128, 4);
INSERT INTO nm_action_roles (aid, rid) VALUES (129, 4);
INSERT INTO nm_action_roles (aid, rid) VALUES (6, 2);
INSERT INTO nm_user_roles (uid, rid) VALUES (1, 1);
INSERT INTO nm_user_usergroups (uid, gid) VALUES (1, 3);
INSERT INTO profiles (uuid, id, first_name, last_name, gender, birthday, address, phone, email, web, uid, gid) VALUES ('5fd659ed9184493fa2d32028d833d91e', 1, '', '', NULL, NULL, '', '', NULL, '', 1, NULL);
"""
DELETES = """"""


def iter_statements(stmts):
    for st in [x for x in stmts.split('\n') if x]:
        op.execute(st)


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('updated', sa.DateTime(), nullable=True),
    sa.Column('uuid', sa.CHAR(length=32), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.Column('uid', sa.Integer(), nullable=True),
    sa.Column('gid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['gid'], ['usergroups.id'], name='fk_comments_gid_usergroups', use_alter=True),
    sa.ForeignKeyConstraint(['parent_id'], ['comments.id'], ),
    sa.ForeignKeyConstraint(['uid'], ['users.id'], name='fk_comments_uid_users', use_alter=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uuid')
    )
    op.create_table('profiles',
    sa.Column('uuid', sa.CHAR(length=32), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('gender', sa.Integer(), nullable=True),
    sa.Column('birthday', sa.Date(), nullable=True),
    sa.Column('address', sa.Text(), nullable=True),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('web', sa.String(), nullable=True),
    sa.Column('uid', sa.Integer(), nullable=True),
    sa.Column('gid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['gid'], ['usergroups.id'], name='fk_profiles_gid_usergroups', use_alter=True),
    sa.ForeignKeyConstraint(['uid'], ['users.id'], name='fk_profiles_uid_users', use_alter=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uuid')
    )
    op.create_table('roles',
    sa.Column('uuid', sa.CHAR(length=32), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('label', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('admin', sa.Boolean(), nullable=True),
    sa.Column('uid', sa.Integer(), nullable=True),
    sa.Column('gid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['gid'], ['usergroups.id'], name='fk_roles_gid_usergroups', use_alter=True),
    sa.ForeignKeyConstraint(['uid'], ['users.id'], name='fk_roles_uid_users', use_alter=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('label'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('uuid')
    )
    op.create_table('sprints',
    sa.Column('uuid', sa.CHAR(length=32), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start', sa.Date(), nullable=True),
    sa.Column('end', sa.Date(), nullable=True),
    sa.Column('strength', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('size', sa.Integer(), nullable=True),
    sa.Column('uid', sa.Integer(), nullable=True),
    sa.Column('gid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['gid'], ['usergroups.id'], name='fk_sprints_gid_usergroups', use_alter=True),
    sa.ForeignKeyConstraint(['uid'], ['users.id'], name='fk_sprints_uid_users', use_alter=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uuid')
    )
    op.create_table('user_settings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('settings', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('usergroups',
    sa.Column('uuid', sa.CHAR(length=32), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('uid', sa.Integer(), nullable=True),
    sa.Column('gid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['gid'], ['usergroups.id'], name='fk_usergroups_gid_usergroups', use_alter=True),
    sa.ForeignKeyConstraint(['uid'], ['users.id'], name='fk_usergroups_uid_users', use_alter=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('uuid')
    )
    op.create_table('versions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('values', sa.Text(), nullable=False),
    sa.Column('author', sa.String(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('estimatelog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sprint_id', sa.Integer(), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('estimate', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['sprint_id'], ['sprints.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('modules',
    sa.Column('uuid', sa.CHAR(length=32), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('clazzpath', sa.String(), nullable=False),
    sa.Column('label', sa.String(), nullable=False),
    sa.Column('label_plural', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('str_repr', sa.String(), nullable=False),
    sa.Column('display', sa.String(), nullable=False),
    sa.Column('default_gid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['default_gid'], ['usergroups.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('clazzpath'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('uuid')
    )
    op.create_table('users',
    sa.Column('uuid', sa.CHAR(length=32), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('login', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('activated', sa.Boolean(), nullable=True),
    sa.Column('activation_token', sa.String(), nullable=False),
    sa.Column('default_gid', sa.Integer(), nullable=True),
    sa.Column('sid', sa.Integer(), nullable=True),
    sa.Column('last_login', sa.DateTime(), nullable=True),
    sa.Column('uid', sa.Integer(), nullable=True),
    sa.Column('gid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['default_gid'], ['usergroups.id'], ),
    sa.ForeignKeyConstraint(['gid'], ['usergroups.id'], name='fk_users_gid_usergroups', use_alter=True),
    sa.ForeignKeyConstraint(['sid'], ['user_settings.id'], ),
    sa.ForeignKeyConstraint(['uid'], ['users.id'], name='fk_users_uid_users', use_alter=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('login'),
    sa.UniqueConstraint('uuid')
    )
    op.create_table('actions',
    sa.Column('uuid', sa.CHAR(length=32), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mid', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('url', sa.String(), nullable=False),
    sa.Column('icon', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('bundle', sa.Boolean(), nullable=False),
    sa.Column('display', sa.String(), nullable=False),
    sa.Column('permission', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['mid'], ['modules.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uuid')
    )
    op.create_table('forms',
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('updated', sa.DateTime(), nullable=True),
    sa.Column('uuid', sa.CHAR(length=32), nullable=True),
    sa.Column('review_state_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('definition', sa.Text(), nullable=True),
    sa.Column('mid', sa.Integer(), nullable=True),
    sa.Column('uid', sa.Integer(), nullable=True),
    sa.Column('gid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['gid'], ['usergroups.id'], name='fk_forms_gid_usergroups', use_alter=True),
    sa.ForeignKeyConstraint(['mid'], ['modules.id'], ),
    sa.ForeignKeyConstraint(['uid'], ['users.id'], name='fk_forms_uid_users', use_alter=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uuid')
    )
    op.create_table('nm_user_roles',
    sa.Column('uid', sa.Integer(), nullable=True),
    sa.Column('rid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['rid'], ['roles.id'], ),
    sa.ForeignKeyConstraint(['uid'], ['users.id'], )
    )
    op.create_table('nm_user_usergroups',
    sa.Column('uid', sa.Integer(), nullable=True),
    sa.Column('gid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['gid'], ['usergroups.id'], ),
    sa.ForeignKeyConstraint(['uid'], ['users.id'], )
    )
    op.create_table('password_reset_requests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uid', sa.Integer(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('token', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['uid'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tags',
    sa.Column('uuid', sa.CHAR(length=32), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('type', sa.Integer(), nullable=True),
    sa.Column('mid', sa.Integer(), nullable=True),
    sa.Column('uid', sa.Integer(), nullable=True),
    sa.Column('gid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['gid'], ['usergroups.id'], name='fk_tags_gid_usergroups', use_alter=True),
    sa.ForeignKeyConstraint(['mid'], ['modules.id'], ),
    sa.ForeignKeyConstraint(['uid'], ['users.id'], name='fk_tags_uid_users', use_alter=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uuid')
    )
    op.create_table('tasks',
    sa.Column('uuid', sa.CHAR(length=32), nullable=True),
    sa.Column('task_state_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), server_default='', nullable=False),
    sa.Column('description', sa.Text(), server_default='', nullable=False),
    sa.Column('priority', sa.Integer(), nullable=True),
    sa.Column('severity', sa.Integer(), nullable=True),
    sa.Column('resolution', sa.Integer(), nullable=True),
    sa.Column('estimate', sa.Integer(), nullable=True),
    sa.Column('assignee_id', sa.Integer(), nullable=True),
    sa.Column('uid', sa.Integer(), nullable=True),
    sa.Column('gid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['assignee_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['gid'], ['usergroups.id'], name='fk_tasks_gid_usergroups', use_alter=True),
    sa.ForeignKeyConstraint(['uid'], ['users.id'], name='fk_tasks_uid_users', use_alter=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uuid')
    )
    op.create_table('nm_action_roles',
    sa.Column('aid', sa.Integer(), nullable=True),
    sa.Column('rid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['aid'], ['actions.id'], ),
    sa.ForeignKeyConstraint(['rid'], ['roles.id'], )
    )
    op.create_table('nm_task_comments',
    sa.Column('iid', sa.Integer(), nullable=True),
    sa.Column('cid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cid'], ['comments.id'], ),
    sa.ForeignKeyConstraint(['iid'], [u'tasks.id'], )
    )
    op.create_table('nm_task_sprints',
    sa.Column('task_id', sa.Integer(), nullable=True),
    sa.Column('sprint_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['sprint_id'], ['sprints.id'], ),
    sa.ForeignKeyConstraint(['task_id'], ['tasks.id'], )
    )
    op.create_table('nm_task_tags',
    sa.Column('iid', sa.Integer(), nullable=True),
    sa.Column('tid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['iid'], [u'tasks.id'], ),
    sa.ForeignKeyConstraint(['tid'], ['tags.id'], )
    )
    op.create_table('nm_task_users',
    sa.Column('task_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['task_id'], ['tasks.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], )
    )
    ### end Alembic commands ###
    iter_statements(INSERTS)


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('nm_task_users')
    op.drop_table('nm_task_tags')
    op.drop_table('nm_task_sprints')
    op.drop_table('nm_task_comments')
    op.drop_table('nm_action_roles')
    op.drop_table('tasks')
    op.drop_table('tags')
    op.drop_table('password_reset_requests')
    op.drop_table('nm_user_usergroups')
    op.drop_table('nm_user_roles')
    op.drop_table('forms')
    op.drop_table('actions')
    op.drop_table('users')
    op.drop_table('modules')
    op.drop_table('estimatelog')
    op.drop_table('versions')
    op.drop_table('usergroups')
    op.drop_table('user_settings')
    op.drop_table('sprints')
    op.drop_table('roles')
    op.drop_table('profiles')
    op.drop_table('comments')
    ### end Alembic commands ###
    iter_statements(DELETES)
