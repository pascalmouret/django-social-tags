# -*- coding: utf-8 -*-
__author__ = 'Pascal Mouret'
__version__ = '0.2a.1'


from social_tags import networks


class MetaObject(object):

    def __init__(self, settings):
        self.settings = settings

    @property
    def objects(self):
        objects = []
        for type, object in networks.AVAILABLE.iteritems():
            objects.append(getattr(networks, object)(**self.settings))
        return objects