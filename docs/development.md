# TODO


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

## Запуск

Поднять все описанные сервисы
```
cd development
docker compose up --build
```


### Запуск миграций для БД md

```
cd development/entrypoints/md
make venv-init
make run-tests
make alembic-upgrade-heads
```
