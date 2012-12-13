# -*- coding: utf-8 -*-
from social_tags import settings


def social(request):
    from social_tags.defaults import DEFAULT_SETTINGS as args
    return {'social_tags': args}