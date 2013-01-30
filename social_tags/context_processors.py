# -*- coding: utf-8 -*-


def social(request):
    from social_tags.networks import networks
    return {'social_tags': networks.get_defaults()}