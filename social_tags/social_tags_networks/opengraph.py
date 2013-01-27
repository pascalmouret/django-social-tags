# -*- coding: utf-8 -*-
from social_tags.networks import Network, networks


class OpenGraph(Network):
    name = 'opengraph'
    template = 'social_tags/networks/opengraph.html'

    def prepare_context(self, context):
        for key, value in context.iteritems():
            context[key] = value
        context['locales'] = [l for l in context['locales'] if l != context['locale']]
        return context
networks.register(OpenGraph)