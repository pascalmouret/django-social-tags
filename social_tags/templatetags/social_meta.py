# -*- coding: utf-8 -*-
from django import template
from django.template.loader import get_template
from django.template.context import Context

from sekizai.templatetags.sekizai_tags import AddData

from social_tags import MetaObject, settings


register = template.Library()


@register.simple_tag(takes_context=True)
def render_meta_tags(context, data):
    args = context['social_tags']
    for key, value in data:
        args[key] = value
    t = get_template('social_tags/meta.html')
    c = Context({'objects': MetaObject(args).objects})
    return t.render(c)


class SetTag(AddData):
    name = 'set_tag'

    def render_tag(self, context, key, value):
        varname = getattr(settings, 'SEKIZAI_VARNAME', 'SEKIZAI_CONTENT_HOLDER')
        context[varname]['social_tags'].append((key, value))
        return ''
register.tag(SetTag)