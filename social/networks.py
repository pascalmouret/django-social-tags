# -*- coding: utf-8 -*-
from social.objects import RenderObject


AVAILABLE = {
    'facebook': 'social.networks.Facebook',
    'google': 'social.networks.Google',
}


class Facebook(RenderObject):
    template = 'social/networks/facebook.html'

class Google(RenderObject):
    template = 'social/networks/google.html'