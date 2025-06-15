import os

from pydantic_settings import BaseSettings


class DataBaseSettings(BaseSettings):
    DATABASE_HOST: str
    DATABASE_PORT: int | None
    DATABASE_NAME: str
    DATABASE_USER: str
    DATABASE_PASS: str

    SA_LOGGING_LEVEL: str = 'INFO'
    SA_ECHO: bool = True
    SA_ECHO_POOL: bool = True

    @property
    def database_url(self):
        port_url = (
            'postgresql+psycopg://'
            '{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
            '?application_name={app_name}'
        )
        without_port_url = (
            'postgresql+psycopg://{db_user}:{db_pass}@{db_host}/{db_name}'
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

    @property
    def LOGGING_CONFIG(self):
        config = {
            'loggers': {
                'sqlalchemy.engine': {
                    'level': self.SA_LOGGING_LEVEL,
                    'handlers': ['default'],
                    'propagate': False,
                }
            }
        }
        return config
