# -*- coding: utf-8 -*-
from social_tags import settings


def social(request):
    from social_tags.defaults import DEFAULT_SETTINGS as args
    if settings.USE_CMS and hasattr(request, 'current_page'):
        from social_tags.cms_helper import SocialPageSettings
        page = SocialPageSettings.objects.get_or_create(page=request.current_page)[0]
        args = dict(args.items() + page.settings.items())
    return {'social_tags': args}