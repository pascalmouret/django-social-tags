# -*- coding: utf-8 -*-
from django.conf import settings


def set_sekizai_data(context, key, value, network=None):
    varname = getattr(settings, 'SEKIZAI_VARNAME', 'SEKIZAI_CONTENT_HOLDER')
    context[varname]['social_tags'].append((key, value, network))