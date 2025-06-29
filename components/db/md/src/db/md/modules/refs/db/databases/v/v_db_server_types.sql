create or replace view md.v_db_server_types
as
/*
## Создал
2025, 13 июня: Почекутов А.В.

## Описание
Сводное представление о типах серверов БД.

## История изменения
гггг, дд месяц:

## Примеры использования
select * from md.v_db_server_types;

*/
select st.id, st.ident, vd.name as vendor, st.note,
	st.modified_at, modified_by.name as modified_by,
	st.created_at, created_by.name as created_by,
	st.position,
	st.deleted
from md.db_server_types st
inner join md.db_vendors vd on vd.id=st.vendor_id
inner join md.users modified_by on modified_by.id=st.modified_by_id
inner join md.users created_by on created_by.id=st.created_by_id
;
