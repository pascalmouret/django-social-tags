# -*- coding: utf-8 -*-
from django.conf import settings


DEFAULT_DEFAULT_IMAGE = ''


DEFAULT_IMAGE = getattr(settings, 'SOCIAL_TAGS_DEFAULT_IMAGE', DEFAULT_DEFAULT_IMAGE)