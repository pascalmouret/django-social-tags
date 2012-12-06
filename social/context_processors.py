# -*- coding: utf-8 -*-
def social(request):
    from social.defaults import DEFAULT_SETTINGS
    return {'social': DEFAULT_SETTINGS}