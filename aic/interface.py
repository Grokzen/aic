# -*- coding: utf-8 -*-

from aic.exceptions import AicModuleException


class AicModule(object):

    def __init__(self):
        pass

    def run(self):
        raise AicModuleException("Must be overridden in subclass")

    def module_name(self):
        """
        Default to class name but can be overridden in subclass
        """
        return str(self.__class__.__name__)
