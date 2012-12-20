# -*- coding: utf-8 -*-
from django import template
from django.template.loader import get_template
from django.template.context import Context

from sekizai.templatetags.sekizai_tags import AddData
from classytags.core import Options
from classytags.arguments import Argument
from classytags.helpers import InclusionTag

from social_tags import networks, settings


register = template.Library()


class MetaObject(object):

    def __init__(self, kwargs):
        self.kwargs = kwargs

    @property
    def objects(self):
        objects = []
        for type, object in networks.AVAILABLE.iteritems():
            objects.append(getattr(networks, object)(**self.kwargs))
        return objects


class RenderMetaTags(InclusionTag):
    name = 'render_meta_tags'
    template = 'social_tags/meta.html'

    options = Options(
        Argument('data'),
    )

    def get_context(self, context, data):
        kwargs = context['social_tags']
        kwargs.update(self.get_request_data(context['request']))
        for key, value in data:
            kwargs[key] = value
        kwargs['request'] = context['request']
        return {'objects': MetaObject(kwargs).objects}

    def get_request_data(self, request):
        data = {}
        data['url'] = request.build_absolute_uri()
        data['locale'] = request.LANGUAGE_CODE
        return data
register.tag(RenderMetaTags)


class SetTag(AddData):
    name = 'set_tag'

    def render_tag(self, context, key, value):
        varname = getattr(settings, 'SEKIZAI_VARNAME', 'SEKIZAI_CONTENT_HOLDER')
        context[varname]['social_tags'].append((key, value))
        return ''
register.tag(SetTag)