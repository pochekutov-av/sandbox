DO LANGUAGE plpgsql $$
DECLARE
	_now timestamp;
	_user_id int;
BEGIN
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
		2, _now, _user_id, _now, _user_id, false,
		'app2', 'Приложение2'
	);
END;
$$;