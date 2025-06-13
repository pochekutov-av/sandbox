
### Отказаться от sa.Tables в тестах, в пользу своего типа

В своем типе указывать order_by используемый по умолчанию.
TestCase.fetchall - обязан делать select с указанием order_by

### entrypoints.create_routines должен уметь учитывать зависимости.

```
dependences = [
    (some, depend_on),
    (views.v_db_databases, views.v_db_server_types)
 ]
```