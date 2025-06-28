
/*
        django_content_type
*/

CREATE TEMP TABLE temp_django_content_type(
	id int,
	app_label varchar,
	model varchar
) ON COMMIT  DROP;

INSERT INTO temp_django_content_type(id, app_label, model)
VALUES
	(1, 'admin', 'logentry'),
	(2,'auth','permission'),
	(3,'auth','group'),
	(4,'contenttypes','contenttype'),
	(5,'sessions','session'),
	(6,'md','user');

-- Добавим то чего нет (если что-то есть оставляем без изменений)
INSERT INTO md.django_content_type(
	id, app_label, model
)
SELECT
	d.id, d.app_label, d.model
FROM temp_django_content_type d
LEFT JOIN md.django_content_type be_there ON be_there.id=d.id
WHERE be_there.id IS NULL;

-- Проставим актуальное значение последовательности id
SELECT
    setval(
        pg_get_serial_sequence('md.django_content_type', 'id'),
        coalesce(max(id),0) + 1,
        false
    )
FROM md.django_content_type;



/*
        auth_permission
*/

CREATE TEMP TABLE temp_auth_permission(
	name varchar,
	content_type_id int,
	codename varchar
) ON COMMIT  DROP;

INSERT INTO temp_auth_permission(name, content_type_id, codename)
VALUES
	('Can add log entry', 1, 'add_logentry'),
	('Can change log entry', 1, 'change_logentry'),
	('Can delete log entry', 1, 'delete_logentry'),
	('Can view log entry', 1, 'view_logentry'),
	('Can add permission', 2, 'add_permission'),
	('Can change permission', 2, 'change_permission'),
	('Can delete permission', 2, 'delete_permission'),
	('Can view permission', 2, 'view_permission'),
	('Can add group', 3, 'add_group'),
	('Can change group', 3, 'change_group'),
	('Can delete group', 3, 'delete_group'),
	('Can view group', 3, 'view_group'),
	('Can add content type', 4, 'add_contenttype'),
	('Can change content type', 4, 'change_contenttype'),
	('Can delete content type', 4, 'delete_contenttype'),
	('Can view content type', 4, 'view_contenttype'),
	('Can add session', 5, 'add_session'),
	('Can change session', 5, 'change_session'),
	('Can delete session', 5, 'delete_session'),
	('Can view session', 5, 'view_session'),
	('Can add user', 6, 'add_user'),
	('Can change user', 6, 'change_user'),
	('Can delete user', 6, 'delete_user'),
	('Can view user', 6, 'view_user');

-- Добавим то чего нет, если что-то есть оставляем без изменений
INSERT INTO md.auth_permission(
	name, content_type_id, codename
)
SELECT
	d.name, d.content_type_id, d.codename
FROM temp_auth_permission d
LEFT JOIN md.auth_permission be_there ON be_there.codename=d.codename
WHERE be_there.codename IS NULL;



/*
        django_migrations
*/

CREATE TEMP TABLE temp_django_migrations(
	app varchar,
	name varchar
) ON COMMIT  DROP;

INSERT INTO temp_django_migrations(app, name)
VALUES
	('md', '0001_initial'),
	('contenttypes', '0001_initial'),
	('admin', '0001_initial'),
	('admin', '0002_logentry_remove_auto_add'),
	('admin', '0003_logentry_add_action_flag_choices'),
	('contenttypes', '0002_remove_content_type_name'),
	('auth', '0001_initial'),
	('auth', '0002_alter_permission_name_max_length'),
	('auth', '0003_alter_user_email_max_length'),
	('auth', '0004_alter_user_username_opts'),
	('auth', '0005_alter_user_last_login_null'),
	('auth', '0006_require_contenttypes_0002'),
	('auth', '0007_alter_validators_add_error_messages'),
	('auth', '0008_alter_user_username_max_length'),
	('auth', '0009_alter_user_last_name_max_length'),
	('auth', '0010_alter_group_name_max_length'),
	('auth', '0011_update_proxy_permissions'),
	('auth', '0012_alter_user_first_name_max_length'),
	('sessions', '0001_initial')
;

-- Добавим то чего нет, если что-то есть оставляем без изменений
INSERT INTO md.django_migrations(
	app, name, applied
)
SELECT
	d.app, d.name, CURRENT_TIMESTAMP
FROM temp_django_migrations d
LEFT JOIN md.django_migrations be_there ON be_there.app=d.app AND be_there.name=d.name
WHERE be_there.app IS NULL;


-- Проставим актуальное значение последовательности id
SELECT
    setval(
        pg_get_serial_sequence('md.django_migrations', 'id'),
        coalesce(max(id),0) + 1,
        false
    )
FROM md.django_migrations;


