# -*- coding: utf-8 -*-
from django import template

from classytags.arguments import KeywordArgument

from social_tags.utils import set_sekizai_data
from social_tags.templatetags.helpers import BaseSetter


register = template.Library()


class TwitterSummaryCard(BaseSetter):
    name = 'twitter_summary'

    settings = (
        (KeywordArgument('description', required=False), None),
        (KeywordArgument('image', required=False), None),
        (KeywordArgument('url', required=False), None),
        (KeywordArgument('title', required=False), None),
        (KeywordArgument('site', required=False), 'twitter'),
        (KeywordArgument('creator', required=False), 'twitter'),
        )

    def render_tag(self, context, **kwargs):
        set_sekizai_data(context, 'card', 'summary', 'twitter')
        return ''
register.tag(TwitterSummaryCard)