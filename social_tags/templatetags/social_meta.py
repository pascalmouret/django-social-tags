# -*- coding: utf-8 -*-
from django import template
from django.template.loader import get_template
from django.template.context import Context

from social_tags import MetaObject, settings


register = template.Library()


@register.simple_tag(takes_context=True)
def social_meta_tags(context):
    args = context['social_tags']
    if settings.USE_CMS and context['request'].current_page:
        from social_tags.cms_helper import SocialPageSettings
        page = SocialPageSettings.objects.get_or_create(page=context['request'].current_page)[0]
        args = dict(args.items() + page.settings.items())
    t = get_template('social_tags/meta.html')
    c = Context({'objects': MetaObject(args).objects})
    return t.render(c)