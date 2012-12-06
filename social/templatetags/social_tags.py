# -*- coding: utf-8 -*-
from django import template
from django.template.loader import get_template
from django.template.context import Context

from social import MetaObject


register = template.Library()


@register.simple_tag(takes_context=True)
def social_meta_tags(context):
    t = get_template('social/meta.html')
    c = Context({'objects': MetaObject(context['social']).objects})
    return t.render(c)