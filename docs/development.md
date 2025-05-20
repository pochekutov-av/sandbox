
# TODO

## Запуск

Поднять все описанные сервисы
```
cd development
docker compose up --build
```


### БД Master Data


Создать с нуля схему БД и загрузить начальные данные:
```
cd development/entrypoints/md
make create_all

```


Запуск миграций:
```
cd development/entrypoints/md
make venv-init
make lint run-tests
make alembic-upgrade-heads
```



## Настройки для запуска x86 (ms sql server) на Apple Silicon

```
 softwareupdate --install-rosetta
```

Затем в настройках Docker:

```
General > Virtual Machine Options
    Choose Virtual Machine Manager (VMM)
        [ ]  Docker VMM
        [*] Apple Virtualization framework
        [ ] QEMU (Legacy)
        
        [X] Use Rosetta for x86_64/amd64 emulation on Apple Silicon
        
        Choose file sharing implementation for your containers
        [*] VirtioFS
        [ ] gRPC FUSE
        [ ] osxfs (Legacy)
```

В описании сервиса обязательно указать платформу:
```
    database-source-mssql-2019:
        ...
        platform: linux/amd64
```

