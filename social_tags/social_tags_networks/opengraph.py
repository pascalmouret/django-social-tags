# -*- coding: utf-8 -*-
from social_tags.networks import Network, networks, SocialTagsValidationError


class OpenGraph(Network):
    name = 'opengraph'
    template = 'social_tags/networks/opengraph.html'

    def prepare_context(self, context):
        for key, value in context.iteritems():
            context[key] = value
        context['locales'] = [l for l in context['locales'] if l != context['locale']]
        return context

    def debug(self, context):
        if not hasattr(context, 'url'):
            raise SocialTagsValidationError('The url settings in required.')
        if not hasattr(context, 'title'):
            raise SocialTagsValidationError('The title setting is required.')
        if not hasattr(context, 'locale'):
            raise SocialTagsValidationError('The locale setting in required.')
networks.register(OpenGraph)