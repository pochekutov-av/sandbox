import sys

from alembic.config import CommandLine, Config

from db.md.md.settings import DataBaseSettings


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
            'db.md.md.migrations:data;'
            'db.md.md.migrations:modules;'
            'db.md.md.migrations:schema;'
        )
    )
    return config


if __name__ == '__main__':    # pragma: no cover
    cli = CommandLine()
    cli.run_cmd(make_config(), cli.parser.parse_args(sys.argv[1:]))
