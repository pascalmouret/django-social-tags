# -*- coding: utf-8 -*-
from django.conf import settings


DEFAULT_DEFAULT_IMAGE = ''

DEFAULT_USE_CMS = False


DEFAULT_IMAGE = getattr(settings, 'SOCIAL_TAGS_DEFAULT_IMAGE', DEFAULT_DEFAULT_IMAGE)
USE_CMS = getattr(settings, 'SOCIAL_TAGS_USE_CMS', 'cms' in settings.INSTALLED_APPS)