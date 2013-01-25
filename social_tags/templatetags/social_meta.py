# -*- coding: utf-8 -*-
from django import template
from django.contrib.sites.models import get_current_site

from sekizai.templatetags.sekizai_tags import AddData
from classytags.core import Options
from classytags.helpers import InclusionTag, Tag

from social_tags import networks, settings
from social_tags.utils import set_sekizai_data


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
        set_sekizai_data(context, key, value)
        return ''
register.tag(SetTag)


class BaseSetter(Tag):
    arguments = {}

    def __init__(self, *args, **kwargs):
        options = ()
        for setting in self.settings:
            self.arguments[setting[0].name] = setting[1]
            options = options + (setting[0],)
        self.options = Options(*options)
        super(BaseSetter, self).__init__(*args, **kwargs)

    def render(self, context, **kwargs):
        items = self.kwargs.items()
        kwargs = dict([(key, value.resolve(context)) for key, value in items])
        kwargs.update(self.blocks)
        for key, value in kwargs.items():
            print '%s %s' % (key, value)
            if not value == {}:
                set_sekizai_data(context, key, value[key], self.arguments[key])
        return self.render_tag(context, **kwargs)


#######################################
# Open Graph
#######################################

class CustomOpenGraph(AddData):
    name = 'opengraph'

    def render_tag(self, context, key, value):
        set_sekizai_data(context, key, value, 'opengraph')
        return ''
register.tag(CustomOpenGraph)

