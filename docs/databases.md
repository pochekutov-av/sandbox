## Образы docker

{% list tabs %}

- Postgres

  Доступные [образы](https://hub.docker.com/_/postgres/tags).

- MS SQL

  Доступные [образы](https://mcr.microsoft.com/v2/mssql/server/tags/list).
  Переменные окружения доступные для образа описаны в [статье](https://learn.microsoft.com/ru-ru/sql/linux/sql-server-linux-configure-environment-variables?view=sql-server-linux-ver15).

{% endlist %}

## Соглашения проекта "database".

Одна схема БД представлена одним пакетом python.

Имя пакета формируется по правилу db_{project-ident}_{schema},
например db_p123_app (в проекте №123 основная схема приложения app).

При создании пакетов нужно использовать [namespace](https://packaging.python.org/en/latest/guides/packaging-namespace-packages/),
чтобы можно было "from db.the_project.the_schema.schema.tables import some_table".

Структура проекта:
  - entrypoints - входные точки для запуска миграции и других задач
  - fixtures - варианты инициализации БД (с нуля, для тестов)
  - migrations - миграции
  - modules - объекты БД, функции процедуры и т.п.
  - schema - описание схемы БД, таблицы, индексы

Имя таблицам даем во множественном числе, просто так договариваемся (
как аргумент единственно число может конфликтовать с ключевыми словами чаще).

При описании таблиц не используем напрямую импорты из sqlalchemy, нужные типы
импортируем из metadata схемы. Что позволит делать более стандартизовано.

Миграции разделяем на три [папки-ветки](https://alembic.sqlalchemy.org/en/latest/branches.html):
  - schema, схема БД - таблицы и индексы;
  - data, данные приложения (инициализация начальных, bulk load);
  - modules, модулем называем набор процедур, функций, представлений (sp, fn,
v), объединенных единых смыслом (например для конкретного справочника);

Миграции структурируем по вложенным папкам, в имени файла содержится время
yyyy/mm/dd/hhmm-{revision}_slug.py.


### Работа с миграциями Alembic

Создать пустую начальную миграцию для конкретной ветви:
```
python -m db.md.md.entrypoints.alembic revision -m "init" --head=base --branch-label=schema --version-path=src/db/md/md/migrations/schema
python -m db.md.md.entrypoints.alembic revision -m "init" --head=base --branch-label=data --version-path=src/db/md/md/migrations/data
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
python -m db.md.md.entrypoints.alembic revision -m "some"  --head data@head
```

Создать с autogenerate
```
python -m db.md.md.entrypoints.alembic revision --autogenerate -m "base tables" --head schema@head
```

Откатить 1 миграцию в ветке schema:
```
python -m db.md.md.entrypoints.alembic downgrade schema@-1
```

Откатить все миграции:
```
python -m db.md.md.entrypoints.alembic downgrade base
```

### Информация о версии сервера, имени БД

{% list tabs %}

- Postgres

  TODO

- MS SQL

Версия сервера:
```
SELECT @@VERSION;
```

Имя БД:
```
SELECT DB_NAME();
```

- Oracle

Версия сервера:
```
SELECT * FROM v$version;
SELECT * FROM product_component_version;
```

Имя БД:
```
SELECT * FROM global_name;
SELECT ora_database_name FROM dual;
SELECT * FROM v$database;
```

{% endlist %}
