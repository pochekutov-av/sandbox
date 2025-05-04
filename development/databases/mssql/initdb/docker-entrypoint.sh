#!/bin/bash
set -Eeo pipefail

export PATH=$PATH:/opt/mssql-tools/bin/

docker_server_ready() {
  for i in {1..50}; do
    echo "TRY CONNECT to MS SQL server, № ${i}"
    if sqlcmd -S "${DATABASE_HOST}" -U "${DATABASE_USER}" -P "${DATABASE_PASS}" -d master -Q "SELECT @@servername;"; then
      echo "SUCCESS."
      break
    else
      echo "FAIL, wait and retry ..."
      sleep 1
    fi
  done
}

docker_process_init_files() {
        printf '\n'
        local f
        for f; do
                case "$f" in
                        *.sql)     printf '%s: running %s\n' "$0" "$f"; docker_process_sql -i "$f"; printf '\n' ;;
                        *)         printf '%s: ignoring %s\n' "$0" "$f" ;;
                esac
                printf '\n'
        done
}

docker_process_sql() {
  sqlcmd -S "${DATABASE_HOST}" -U "${DATABASE_USER}" -P "${DATABASE_PASS}" -d master "$@"
}

_main() {
  docker_server_ready
  docker_process_init_files /docker-entrypoint-initdb.d/*
}

_main "$@"
