

## Образы docker

{% list tabs %}

- Postgres

  Доступные [образы](https://hub.docker.com/_/postgres/tags).

- MS SQL

  Доступные [образы](https://mcr.microsoft.com/v2/mssql/server/tags/list).
  Переменные окружения доступные для образа описаны в [статье](https://learn.microsoft.com/ru-ru/sql/linux/sql-server-linux-configure-environment-variables?view=sql-server-linux-ver15).

{% endlist %}

## Соглашения проекта "database".

Одна схема БД представлено одним пакетом python.

Имя пакета формируется по правилу db_{project-ident}_{schema},
например db_p123_app (в проекте №123 основная схема пирложения app).

При создании пакетов нужно использовать [namespace](https://packaging.python.org/en/latest/guides/packaging-namespace-packages/),
чтобы можно было "from db.some_project.some_scheme.dd.tables import some_table".

Структура проекта: 
  - dd - data definition, описание таблиц индексов
  - entrypoints - входные точки для запуска миграции и других задач
  - migrations - миграции
  - modules - объекты БД, функции процедуры и т.п.
  - dd/metadata.py - sqlalchemy metadata

Имя таблицам даем во множественном числе, просто так договариваемся (
как аргумент единственно число может конфликтовать с ключевыми словами чаще).

При описании таблиц не используем напрямую импорты из sqlalchemy, нужные типы
импортируем из metadata схемы. Что позволит делать более стандартизовано.

Миграции разделяем над схемой разделяем на три [папки-ветки](https://alembic.sqlalchemy.org/en/latest/branches.html):
  - dd, data definition - создание и модификация схемы БД, индексов
  - dm, data manipulation - изменение содержимого в таблицах
  - modules - изменение процедур, функций, представлений.

Миграции структурируем по вложенным папкам, в имени файла содержится время
yyyy/mm/dd/hhmm-{revision}_slug.py.


### Работа с миграциями Alembic

Создать пустую начальную миграцию для конкретной ветви:
```
python -m db.md.md.entrypoints.alembic revision -m "init" --head=base --branch-label=dd --version-path=src/db/md/md/migrations/dd
python -m db.md.md.entrypoints.alembic revision -m "init" --head=base --branch-label=dm --version-path=src/db/md/md/migrations/dm
python -m db.md.md.entrypoints.alembic revision -m "init" --head=base --branch-label=modules --version-path=src/db/md/md/migrations/modules
```

Применить все миграции для всех ветвей до head:
```
python -m db.md.md.entrypoints.alembic upgrade heads
```

Посмотреть текущую версию состояния БД:
```
python -m db.md.md.entrypoints.alembic current
```

Создать пустую НЕ начальную миграцию для конкретной ветви. Для этого нужно
временно перенести последнюю миграцию из ветки из структуры yyyy/mm/dd в корень,
поскольку в "version locations" не входят вложенные папки.
(FAILED: Path .../migrations/dm/2025/05/07 is not represented in current version locations)
```
python -m db.md.md.entrypoints.alembic revision -m "some"  --head dm@head
```

Создать с autogenerate
```
python -m db.md.md.entrypoints.alembic revision --autogenerate -m "users and sites" --head dd@head
```


Откатить все миграции:
```
python -m db.md.md.entrypoints.alembic downgrade base
```

Откатить 1 миграцию в ветке dd:
```
python -m db.md.md.entrypoints.alembic downgrade dd@-1
```