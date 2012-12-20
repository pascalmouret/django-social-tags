# -*- coding: utf-8 -*-
from django.template.loader import get_template
from django.template.context import Context


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
        return t.render(c)