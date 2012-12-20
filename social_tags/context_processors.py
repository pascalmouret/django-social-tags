# -*- coding: utf-8 -*-


def social(request):
    from social_tags.defaults import DEFAULT_SETTINGS
    return {'social_tags': DEFAULT_SETTINGS}