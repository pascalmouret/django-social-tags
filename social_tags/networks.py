# -*- coding: utf-8 -*-
from social_tags.objects import RenderObject


AVAILABLE = {
    'facebook': 'Facebook',
    'google': 'Google',
}


class Facebook(RenderObject):
    template = 'social_tags/networks/facebook.html'

class Google(RenderObject):
    template = 'social_tags/networks/google.html'