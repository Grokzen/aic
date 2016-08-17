# -*- coding: utf-8 -*-

""" aic - cli.py """

# python std lib
import logging
import logging.config

# 3rd party imports
from docopt import docopt


def parse_cli():
    """
    """
    __docopt__ = """
Usage: aic collect [-m MODULE ...] [options]
       aic list [options]

Arguments:
  -p, --pretty                         Output will be formatted with pprint
  -o FORMAT, --output FORMAT           Format that can be outputed.
                                       One of 'json', 'yaml' [Default: yaml]
  -l LOG_LEVEL, --log-level=LOG_LEVEL  Console logging log level.
                                       One of 'debug', 'info', 'warning', 'error', 'critical', 'quiet'.
                                       [Default: warning]
  -m MODULE, --module MODULE           Run only these modules. Can be specefied multiple times.
  -h, --help                           Show this help message and exit
  -q, --quiet                          Suppress all terminal output
  --version                            Display the version number and exit
  -v, --verbose                        Verbose terminal output (multiple -v increases verbosity)
"""

    # Import aic package
    import aic

    args = docopt(__docopt__, version=aic.__version__)

    aic.init_logging(args['--log-level'].upper(), args['--quiet'])
    log = logging.getLogger(__name__)

    log.debug("Arguments from CLI: %s", args)

    return args


def run(cli_args):
    """
    Split the functionality into 2 methods.

    One for parsing the cli and one that runs the application.
    """
    from aic.core import Core

    c = Core(output_format=cli_args['--output'], pretty_output=cli_args['--pretty'])
    c.load_modules()

    if cli_args['list']:
        c.run_list_command()
    elif cli_args['collect']:
        c.run()
        c.print_data()
    else:
        print("Unknown command...")

    return c


def cli_entrypoint():
    """
    Main entrypoint for script. Used by setup.py to automatically
    create a cli script
    """
    run(parse_cli())
