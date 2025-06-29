import logging.config

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    LOGGING_LEVEL: str = 'DEBUG'

    @property
    def LOGGING_CONFIG(self) -> dict:
        fmt = '%(asctime)s.%(msecs)03d [%(levelname)s]|[%(name)s]: %(message)s'
        datefmt = '%Y-%m-%d %H:%M:%S'
        config = {
            'version': 1,
            'disable_existing_loggers': True,
            'formatters': {
                'default': {
                    'format': fmt,
                    'datefmt': datefmt,
                },
            },
            'handlers': {
                'default': {
                    'class': 'logging.StreamHandler',
                    'level': self.LOGGING_LEVEL,
                    'formatter': 'default',
                    'stream': 'ext://sys.stdout',
                },
            },
            'loggers': {
                '': {
                    'level': self.LOGGING_LEVEL,
                    'handlers': ['default'],
                    'propagate': False
                },
            }
        }
        return config


def configure(*configs: dict):
    result_config = Settings().LOGGING_CONFIG
    for config in configs:
        result_config['formatters'].update(config.get('formatters', {}))
        result_config['handlers'].update(config.get('handlers', {}))
        result_config['loggers'].update(config.get('loggers', {}))
    logging.config.dictConfig(result_config)
