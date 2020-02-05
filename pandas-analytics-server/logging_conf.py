from logging.config import dictConfig


def init_logging():
    logging_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'f': {
                'format': '%(asctime)s [%(levelname)s] %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S'
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'f',
                'level': 'INFO',
            },
            'file': {
                'class': 'logging.handlers.RotatingFileHandler',
                'level': 'INFO',
                'formatter': 'f',
                'filename': 'logs/pandas-plotting-server.log',
                'mode': 'a',
            }
        },
        'root': {
            'handlers': ['file', 'console'],
            'level': 'INFO',
            'propagate': True,
        }
    }
    dictConfig(logging_config)
