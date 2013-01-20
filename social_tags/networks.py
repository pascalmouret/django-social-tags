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
        context['twitter']['width'] = pic.width
        context['twitter']['height'] = pic.height
        return context

    def get_player_context(self, context):
        return context

    def debug(self, context):
        if context['card'] == 'summary':
            if not context['description']:
                raise Exception('Description is required for summary card.')
        if context['card'] == 'photo':
            if not context['image']:
                raise Exception('Image is required for photo card')
        if context['card'] == 'player':
            if not context['twitter']['player'] or not context['twitter']['width'] or not context['twitter']['height']:
                raise Exception('Player, width and height are required for player card')
            if context['twitter']['stream'] and not context['twitter']['content_type']:
                raise Exception('If stream is set, content_type is required.')
