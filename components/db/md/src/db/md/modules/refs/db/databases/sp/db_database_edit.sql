CREATE OR REPLACE PROCEDURE md.db_database_edit
(
	user_id INT,  -- ид пользователя    
	now TIMESTAMPTZ,  -- время начала unit of work 
	mode TEXT,  -- режим работы
				-- add - добавление
				-- change - изменение
				-- delete - пометка удаленным
				-- undelete - восстановление удаленного
	ident VARCHAR(63),
	host TEXT,
	name TEXT,
	port INT,
	type_id SMALLINT,
	mssql_instance TEXT,
	note TEXT,
	INOUT id INT DEFAULT NULL::INT,  -- ид записи
    INOUT errors REFCURSOR DEFAULT NULL::REFCURSOR
)
LANGUAGE plpgsql
AS
$$
DECLARE
	_user_id INT := user_id;
	_now TIMESTAMPTZ := now;
	_mode TEXT := mode;
    _id INT := id;
	_ident VARCHAR(63) := ident;
	_host TEXT := host;
	_name TEXT := name;
	_port INT := port;
	_type_id SMALLINT := type_id;
	_mssql_instance TEXT := mssql_instance;
	_note TEXT := note;
BEGIN
/*
## Создал
2025, 29 июня: Почекутов А.В.

## Описание
Процедура редактирования для справочника [db_databases].

## История изменения
гггг, дд месяц:

## Пример успешного вызова (указываем все возможные параметры)


BEGIN TRANSACTION;
CALL md.db_database_edit(
	user_id => 1::INT,
	now => '20250629 08:01:02'::TIMESTAMPTZ,
    mode => 'add'::TEXT,
	ident =>'the-ident'::VARCHAR,
	host => 'the-host'::TEXT,
	name => 'the-name'::TEXT,
	port => 12345::INT,
	type_id => 2::SMALLINT, 
	mssql_instance => 'the-mssql_instance'::TEXT,
	note => 'the-note'::TEXT
);
--    FETCH ALL FROM errors_cur;
COMMIT TRANSACTION;
-- ROLLBACK;
-- SELECT * FROM md.db_databases;
-- DELETE FROM md.db_databases;


## Посмотреть версии
SELECT 'DROP procedure ' || oid::regprocedure || ';'
FROM   pg_proc
WHERE  proname = 'db_database_edit'  -- name without schema-qualification

*/

	IF _mode = 'add' THEN

		INSERT INTO  md.db_databases (
			created_at, created_by_id, modified_at, modified_by_id, deleted,
			ident, host, name, port, type_id, mssql_instance, note
		)
		VALUES (
			_now, _user_id, _now, _user_id, false,
			_ident , _host, _name, _port, _type_id, _mssql_instance, _note
		) 
		RETURNING db_databases.id 
		INTO db_database_edit.id;

	END IF;


	IF _mode = 'change' THEN

		UPDATE md.db_databases d
			SET 
				modified_at = _now,
				modified_by_id = user_id,
				ident = _ident,
				host = _host,
				name = _name,
				port = _port,
				type_id = _type_id,
				mssql_instance = _mssql_instance,
				note = _note
		WHERE d.id=_id;

	END IF;

END;
$$;