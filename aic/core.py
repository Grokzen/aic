# -*- coding: utf-8 -*-

""" aic - core.py """

from aic.exceptions import AicOutputException

# python std lib
import json
import logging
from pkg_resources import iter_entry_points

# aic modules
from aic.interfaces.saltstack import process_salt_interface

# 3rd party imports
import yaml

log = logging.getLogger(__name__)


class Core(object):

    def __init__(self, output_format=None, pretty_output=None):
        log.debug("Creating new core class")

        # Always default to yaml as output format
        self.output_format = output_format or 'yaml'
        # Only print pretty output if provided by user
        self.pretty_output = pretty_output or False

        # List of all  module classes that is registered through setuptools
        self.modules = []

        self.data = {}

        log.debug(self.output_format)
        log.debug(self.pretty_output)

    def load_modules(self):
        available_modules = []
        for entry_point in iter_entry_points(group='aic.modules', name=None):
            available_modules.append(
                entry_point.load()()
            )

        log.debug("All available aic modules")
        log.debug(available_modules)

        self.modules = available_modules

    def run(self, run_saltstack_interface=False):
        self.data = {}

        if run_saltstack_interface:
            self.data = process_salt_interface()

        for module in self.modules:
            self.data[module.module_name().lower()] = module.run()

    def print_data(self):
        log.debug("Dumping format: {0}".format(self.output_format))
        log.debug("Pretty format: {0}".format(self.pretty_output))

        if self.output_format == 'yaml':
            print(yaml.dump(self.data, default_flow_style=False))
        elif self.output_format == 'json':
            if self.pretty_output:
                print(json.dumps(self.data, indent=2))
            else:
                print(self.data)
        else:
            raise AicOutputException("Unsupported output format")

    def run_list_command(self):
        """
        Inventory all existing modules and return the name of it
        """
        print("*** All available modules ***")
        for module in self.modules:
            print(" - {0}".format(module.module_name()))
