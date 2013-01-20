# -*- coding: utf-8 -*-
from django.template.loader import get_template
from django.template.context import Context
from django.conf import settings


class RenderObject(object):
    template = None

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.request = kwargs['request']

    def prepare_context(self, context):
        return context

    def render(self):
        if not self.template:
            raise Exception('No template defined.')
        t = get_template(self.template)
        c = Context(self.prepare_context(self.kwargs))
        if settings.DEBUG:
            self.debug(c)
        return t.render(c)

    def debug(self, context):
        pass