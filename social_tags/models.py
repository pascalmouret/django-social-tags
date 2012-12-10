# -*- coding: utf-8 -*-
from social_tags import settings


if settings.USE_CMS:
    from social_tags.cms_helper import SocialPageSettings