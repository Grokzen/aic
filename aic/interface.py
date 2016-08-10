# -*- coding: utf-8 -*-

from aic.exceptions import AicModuleException


class AicModule(object):

    def __init__(self):
        pass

    def run(self):
        raise AicModuleException("Must be overridden in subclass")

    def module_name(self):
        raise AicModuleException("Must be overridden in subclass")
