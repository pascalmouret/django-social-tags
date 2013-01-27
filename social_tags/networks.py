# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from django.template.loader import get_template
from django.template.context import Context

from social_tags import settings

import imp


class SocialTagsValidationError(Exception):
    pass


class Network(object):
    name = 'network'
    template = None

    def __init__(self, **context):
        self.context = context
        self.request = context['request']
        if not self.template:
            raise Exception('No template defined.')

    def render(self):
        t = get_template(self.template)
        c = Context(self.prepare_context(self.context))
        if settings.DEBUG:
            self.debug(c)
        return t.render(c)

    def prepare_context(self, context):
        return context

    def debug(self, context):
        pass


class NetworkCollection(object):
    networks = {}
    module_name = 'social_tags_networks'

    _loaded = False

    def __init__(self):
        self._load_modules()

    def register(self, network):
        self.networks[network.name] = network

    def get_enabled(self):
        if not self._loaded:
            self._load_modules()
            self._loaded = True
        enabled = {}
        for name, network in self.networks.items():
            if name in settings.ENABLED_NETWORKS:
                enabled[name] = network
        return enabled

    def _load_modules(self):
        from django.conf import settings as dj_settings
        installed_apps = getattr(dj_settings, 'INSTALLED_APPS', ())
        for app in installed_apps:
            try:
                p = imp.load_module(app, *imp.find_module(app))
                imp.load_module(self.module_name, *imp.find_module(self.module_name, p.__path__))
            except ImportError:
                pass
networks = NetworkCollection()