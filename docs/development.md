## Запуск

Поднять все описанные сервисы
```
cd development
docker compose up --build
```


### Запуск entrypoints:site01, схема master data

Создать на пустой БД последнюю версию схемы и загрузить начальные данные:
```
cd development/entrypoints/site01
make venv-init
make lint test-unit test
make create-tables create-routines loaddata
```

Накатить миграции:
```
cd development/entrypoints/md
make migrate-upgrade-heads
```


## Запуск x86 docker образа на Apple Silicon

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

