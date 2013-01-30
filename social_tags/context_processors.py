# -*- coding: utf-8 -*-


def social(request):
    from social_tags.settings import DEFAULT_CONTEXT
    return {'social_tags': DEFAULT_CONTEXT}