# -*- coding: utf-8 -*-
__author__ = 'Pascal Mouret'
__version__ = '0.1a.0'


from social import networks
from social.utils import get_class


class MetaObject(object):

    def __init__(self, settings):
        self.settings = settings

    @property
    def objects(self):
        objects = []
        for type, object in networks.AVAILABLE.iteritems():
            print object
            objects.append(get_class(object)(**self.settings))
        return objects