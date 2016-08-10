# -*- coding: utf-8 -*-

""" aic """

# python stdlib
import logging
import logging.config
import os
import sys

if sys.version_info[0] < 3:
    # We must force python2 systems to use utf8 encoding instead of default ascii to fix
    # some problems that exists when using utf8 data.
    reload(sys)  # Reload does the trick!  # NOQA
    sys.setdefaultencoding('UTF8')

__author__ = 'Grokzen <Grokzen@gmail.com>'
__version_info__ = (1, 0, 0)
__version__ = '.'.join(map(str, __version_info__))

valid_log_levels = set(['CRITICAL', 'ERROR', 'WARNING', 'ERROR', 'INFO', 'DEBUG'])


def init_logging(log_level_cli, quiet):
    """
    Init logging settings with default set to INFO
    """
    # No CRITICAL level messages should even be sent out
    # TODO: This is not the correct way to do this. Look at NullLogger to see if that works better as a "silent" logger
    if quiet:
        log_level_cli = "CRITICAL"

    if log_level_cli not in valid_log_levels:
        raise Exception("Invalid log level specefied")

    msg = "%(levelname)s - %(name)s:%(lineno)s - %(message)s" if "DEBUG" in os.environ else "%(levelname)s - %(message)s"

    logging_conf = {
        "version": 1,
        "root": {
            "level": log_level_cli,
            "handlers": ["console"]
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": log_level_cli,
                "formatter": "simple",
                "stream": "ext://sys.stdout"
            }
        },
        "formatters": {
            "simple": {
                "format": " {}".format(msg)
            }
        }
    }

    logging.config.dictConfig(logging_conf)
