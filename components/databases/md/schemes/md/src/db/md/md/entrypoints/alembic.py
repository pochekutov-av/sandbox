import os
import sys

from alembic.config import CommandLine, Config
from pydantic_settings import BaseSettings


class DataBaseSettings(BaseSettings):
    DATABASE_HOST: str
    DATABASE_PORT: int | None    # TODO: Не используется нигде
    DATABASE_NAME: str
    DATABASE_USER: str
    DATABASE_PASS: str

    @property
    def database_url(self):
        port_url = (
            'postgresql+psycopg2://'
            '{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
            '?application_name={app_name}'
        )
        without_port_url = (
            'postgresql+psycopg2://{db_user}:{db_pass}@{db_host}/{db_name}'
            '?application_name={app_name}'
        )
        url = port_url if self.DATABASE_PORT else without_port_url

        return url.format(
            db_user=self.DATABASE_USER,
            db_pass=self.DATABASE_PASS,
            db_host=self.DATABASE_HOST,
            db_name=self.DATABASE_NAME,
            db_port=self.DATABASE_PORT,
            app_name=self._get_app_name(),
        )

    def _get_app_name(self) -> str:
        """
        Получение наименование приложения, которое подключается к БД.
        В том числе, наименование пода в OpenShift.
        """
        return os.uname()[1]


class Settings:
    db = DataBaseSettings()


def make_config():
    config = Config()
    config.set_main_option('sqlalchemy.url', Settings.db.database_url)
    config.set_main_option('timezone', 'UTC')
    config.set_main_option(
        'file_template', (
            '%%(year)d_%%(month).2d%%(day).2d_%%(hour).2d%%(minute).2d-'
            '%%(rev)s_%%(slug)s'
        )
    )
    config.set_main_option('script_location', 'db.md.md:migrations')
    config.set_main_option('recursive_version_locations', 'true')
    config.set_main_option('version_path_separator', ';')
    config.set_main_option(
        'version_locations', (
            'db.md.md.migrations:dm;'
            'db.md.md.migrations:dd;'
            'db.md.md.migrations:modules'
        )
    )
    return config


def run_cmd(*args):
    cli = CommandLine()
    cli.run_cmd(make_config(), cli.parser.parse_args(args))


if __name__ == '__main__':
    run_cmd(*sys.argv[1:])
