#!/usr/bin/env bash
# Based on https://github.com/docker-library/postgres/blob/master/docker-entrypoint.sh
set -Eeo pipefail

export  PGPASSWORD="$DATABASE_PASS"

docker_server_ready() {
  for i in {1..50}; do
    echo "TRY CONNECT to PostgreSQL server, № ${i}"
    if psql -h "$DATABASE_HOST" -p "$DATABASE_PORT" -U "$DATABASE_USER" -d postgres -c "SELECT version();"; then
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
                        *.sql)     printf '%s: running %s\n' "$0" "$f"; docker_process_sql -f "$f"; printf '\n' ;;
                        *)         printf '%s: ignoring %s\n' "$0" "$f" ;;
                esac
                printf '\n'
        done
}

docker_process_sql() {
  psql -h "$DATABASE_HOST" -p "$DATABASE_PORT" -U "$DATABASE_USER" -d postgres "$@"
}

_main() {
  docker_server_ready
  docker_process_init_files /docker-entrypoint-initdb.d/*
}

_main "$@"
