### entrypoints.create_routines должен уметь учитывать зависимости.

```
dependences = [
    (some, depend_on),
    (views.v_db_databases, views.v_db_server_types)
 ]
```




https://stackoverflow.com/questions/70602409/how-do-i-change-the-default-schema-to-custom-schema-in-postgres-from-django-sett


default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'OPTIONS': {
        'options': '-c search_path=custom_schema'
    },
    'NAME': 'name',
    'USER': 'user',
    'PASSWORD': 'password',
   }
}

https://docs.djangoproject.com/en/5.2/topics/db/multi-db/