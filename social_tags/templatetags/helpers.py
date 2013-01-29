# -*- coding: utf-8 -*-
from classytags.core import Options
from classytags.helpers import Tag

from social_tags.utils import set_sekizai_data


class MetaObject(object):

    def __init__(self, **context):
        self.context = context

    @property
    def objects(self):
        objects = []
        for name, cls in networks.get_enabled().items():
            objects.append(cls(**self.context))
        return objects


class BaseSetter(Tag):
    arguments = {}

    def __init__(self, *args, **kwargs):
        options = ()
        for setting in self.settings:
            self.arguments[setting[0].name] = setting[1]
            options = options + (setting[0],)
        self.options = Options(*options)
        super(BaseSetter, self).__init__(*args, **kwargs)

    def render(self, context, **kwargs):
        items = self.kwargs.items()
        kwargs = dict([(key, value.resolve(context)) for key, value in items])
        kwargs.update(self.blocks)
        for key, value in kwargs.items():
            if not value == {}:
                set_sekizai_data(context, key, value[key], self.arguments[key])
        return self.render_tag(context, **kwargs)