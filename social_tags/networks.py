# -*- coding: utf-8 -*-
from django.core.files.images import ImageFile

from social_tags.objects import RenderObject


AVAILABLE = {
    'opengraph': 'OpenGraph',
    'twitter': 'Twitter',
}

class OpenGraph(RenderObject):
    template = 'social_tags/networks/opengraph.html'

    def prepare_context(self, context):
        for key, value in context.iteritems():
            context[key] = value
        context['locales'] = [l for l in context['locales'] if l != context['locale']]
        return context


class Twitter(RenderObject):
    template = 'social_tags/networks/twitter.html'

    def prepare_context(self, context):
        if context['card'] == 'summary':
            return self.get_summary_context(context)
        if context['card'] == 'photo':
            return self.get_photo_context(context)
        if context['card'] == 'player':
            return self.get_player_context(context)

    def get_summary_context(self, context):
        return context

    def get_photo_context(self, context):
        try:
            pic = ImageFile(open(context['image']), 'r')
        except IOError:
            return context
        if not hasattr(context, 'twitter'):
            context['twitter'] = {}
        context['twitter']['width'] = pic.width
        context['twitter']['height'] = pic.height
        return context

    def get_player_context(self, context):
        raise NotImplementedError('Not yet implemented.')