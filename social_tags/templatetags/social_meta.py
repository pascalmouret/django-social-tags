# -*- coding: utf-8 -*-
from django import template
from django.contrib.sites.models import get_current_site

from classytags.core import Options
from classytags.arguments import Argument
from classytags.helpers import InclusionTag, Tag

from social_tags import settings
from social_tags.utils import set_sekizai_data
from social_tags.templatetags.helpers import MetaObject


register = template.Library()


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
        return {'objects': MetaObject(**kwargs).objects}

    def get_request_data(self, request):
        data = {
            'url': request.build_absolute_uri(),
            'locale': request.LANGUAGE_CODE,
            'title': settings.DEFAULT_TITLE or get_current_site(request).name,
        }
        return data
register.tag(RenderMetaTags)


class SetTag(Tag):
    name = 'set_tag'

    options = Options(
        Argument('key'),
        Argument('value'),
        Argument('network'),
    )

    def render_tag(self, context, key, value, network=None):
        set_sekizai_data(context, key, value, network)
        return ''
register.tag(SetTag)