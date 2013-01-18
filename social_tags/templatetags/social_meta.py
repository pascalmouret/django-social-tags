# -*- coding: utf-8 -*-
from django import template
from django.contrib.sites.models import get_current_site

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


#######################################
# Default Tags
#######################################

class RenderMetaTags(InclusionTag):
    name = 'render_meta_tags'
    template = 'social_tags/meta.html'

    options = Options(
        Argument('data'),
    )

    def get_context(self, context, data):
        kwargs = self.get_request_data(context['request'])
        kwargs.update(context['social_tags'])
        for key, value, network in data:
            if network:
                if not hasattr(kwargs, network):
                    kwargs[network] = {}
                kwargs[network][key] = value
            else:
                kwargs[key] = value
        kwargs['request'] = context['request']
        return {'objects': MetaObject(kwargs).objects}

    def get_request_data(self, request):
        data = {
            'url': request.build_absolute_uri(),
            'locale': request.LANGUAGE_CODE,
            'title': settings.DEFAULT_TITLE or get_current_site(request).name,
        }
        return data
register.tag(RenderMetaTags)


class SetTag(AddData):
    name = 'set_tag'

    def render_tag(self, context, key, value):
        varname = getattr(settings, 'SEKIZAI_VARNAME', 'SEKIZAI_CONTENT_HOLDER')
        context[varname]['social_tags'].append((key, value, None))
        return ''
register.tag(SetTag)


#######################################
# Open Graph
#######################################

class CustomOpenGraph(AddData):
    name = 'opengraph'

    def render_tag(self, context, key, value):
        varname = getattr(settings, 'SEKIZAI_VARNAME', 'SEKIZAI_CONTENT_HOLDER')
        context[varname]['social_tags'].append((key, value, 'opengraph'))
        return ''
register.tag(CustomOpenGraph)