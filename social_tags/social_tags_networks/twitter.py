# -*- coding: utf-8 -*-
from django.core.files.images import ImageFile

from social_tags.networks import Network, networks, SocialTagsValidationError


class Twitter(Network):
    name = 'twitter'
    template = 'social_tags/networks/twitter.html'

    def prepare_context(self, context):
        if context['twitter']['card'] == 'summary':
            return self.get_summary_context(context)
        if context['twitter']['card'] == 'photo':
            return self.get_photo_context(context)
        if context['twitter']['card'] == 'player':
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
        if context['twitter']['card'] == 'summary':
            if not context['description']:
                raise SocialTagsValidationError('Description is required for summary card.')
        if context['twitter']['card'] == 'photo':
            if not context['image']:
                raise SocialTagsValidationError('Image is required for photo card')
        if context['twitter']['card'] == 'player':
            if not context['twitter']['player'] or not context['twitter']['width'] or not context['twitter']['height']:
                raise SocialTagsValidationError('Player, width and height are required for player card')
            if context['twitter']['stream'] and not context['twitter']['content_type']:
                raise SocialTagsValidationError('If stream is set, content_type is required.')
networks.register(Twitter)