# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from cms.models.fields import PageField

from filer.fields.image import FilerImageField


class SocialPageSettings(models.Model):
    page = PageField()

    # settings
    options = ['image',]
    image = FilerImageField(verbose_name=_('image'), blank=True, null=True)

    def get_image(self):
        if self.image:
            return self.image.url
        return None

    @property
    def settings(self):
        ret = {}
        for setting in self.options:
            value = getattr(self, setting, False)
            if value:
                ret[setting] = value
        return ret


class SocialPageSettingsAdmin(admin.StackedInline):
    model = SocialPageSettings
    fields = (SocialPageSettings.options)