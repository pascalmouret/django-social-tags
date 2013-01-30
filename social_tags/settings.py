# -*- coding: utf-8 -*-
from django.conf import settings

from social_tags.networks import networks


DEFAULT_DEFAULT_TITLE = None
DEFAULT_DEFAULT_IMAGE = None
DEFAULT_DEFAULT_TYPE = None
DEFAULT_DEFAULT_LOCALE = settings.LANGUAGE_CODE
DEFAULT_DEFAULT_LOCALES = [l[0] for l in settings.LANGUAGES]
DEFAULT_DEFAULT_DESCRIPTION = None

DEFAULT_ENABLED_NETWORKS = (
    'opengraph',
    'twitter',
)


DEBUG = settings.DEBUG

DEFAULT_TITLE = getattr(settings, 'SOCIAL_TAGS_DEFAULT_TITLE', DEFAULT_DEFAULT_TITLE)
DEFAULT_IMAGE = getattr(settings, 'SOCIAL_TAGS_DEFAULT_IMAGE', DEFAULT_DEFAULT_IMAGE)
DEFAULT_TYPE = getattr(settings, 'SOCIAL_TAGS_DEFAULT_TYPE', DEFAULT_DEFAULT_TYPE)
DEFAULT_LOCALE = getattr(settings, 'SOCIAL_TAGS_DEFAULT_LOCALE', DEFAULT_DEFAULT_LOCALE)
DEFAULT_LOCALES = getattr(settings, 'SOCIAL_TAGS_DEFAULT_LOCALES', DEFAULT_DEFAULT_LOCALES)
DEFAULT_DESCRIPTION = getattr(settings, 'SOCIAL_TAGS_DEFAULT_DESCRIPTION', DEFAULT_DEFAULT_DESCRIPTION)

ENABLED_NETWORKS = getattr(settings, 'SOCIAL_TAGS_ENABLED_NETWORKS', DEFAULT_ENABLED_NETWORKS)

DEFAULT_CONTEXT = {
    'type': DEFAULT_TYPE,
    'image': DEFAULT_IMAGE,
    'locales': DEFAULT_LOCALES,
    'description': DEFAULT_DESCRIPTION,
}

DEFAULT_CONTEXT.update(networks.get_defaults())
for network in networks:
    DEFAULT_CONTEXT[network.name].update(getattr(settings, 'SOCIAL_TAGS_%s' % network.name.upper(), {}))
