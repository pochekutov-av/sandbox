DO LANGUAGE plpgsql $$
DECLARE
	_now timestamp;
	_user_id int;
    -- vendors ids:
	_click_house_id int = 1;
	_ms_sql_id int = 2;
	_oracle_id int = 3;
	_postgresql_id int = 4;
	_postgrespro_id int = 5;
BEGIN
/*
Описание: Скрипт инициализации начальных данных.
Добавляет данные для таблиц:
select * from md.users;
select * from md.db_vendors;
select * from md.db_server_types;

Удалить все данные: !!truncate md.users CASCADE!!
*/
	_now = now();
	_user_id = 1;

	/*
		users
	*/
	insert into md.users(
		id, created_at, created_by_id, modified_at, modified_by_id, deleted,
		ident, name
	)
	values(
		_user_id, _now, _user_id, _now, _user_id, false,
		'app', 'Приложение'
	);


	/*
		vendors
	*/
	create temporary table tmp_vendors(id int, name text) on commit drop;
	insert into tmp_vendors(id, name) values
		(_click_house_id, 'Clickhouse'),
		(_ms_sql_id, 'MS SQL'),
        (_oracle_id, 'Oracle'),
        (_postgresql_id, 'PostgreSQL'),
        (_postgrespro_id, 'PostgresPro');

	insert into md.db_vendors(
		id, created_at, created_by_id, modified_at, modified_by_id, deleted,
		position, name
	)
	select
		id, _now, _user_id, _now, _user_id, false,
		id /*position*/, name
	from tmp_vendors;


	/*
		server_types
	*/
	create temporary table tmp_server_types(position int, ident text, vendor_id int, note text) on commit drop;
	insert into  tmp_server_types(position, ident, vendor_id, note) values
		(10, 'pg/16.9', _postgresql_id, 'PostgreSQL 16.9'),
		(10, 'mssql/2019', _ms_sql_id, 'MS-SQL 2019')
		;

	insert into md.db_server_types(
		created_at, created_by_id, modified_at, modified_by_id, deleted,
		position, ident, vendor_id, note
	)
	select
		_now, _user_id, _now, _user_id, false,
		position, ident, vendor_id, note
	from tmp_server_types;

END;
$$;
