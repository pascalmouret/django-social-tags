# -*- coding: utf-8 -*-
from importlib import import_module


def get_class(str):
    modul = '.'.join(str.split('.')[:-1])
    class_name = str.split('.')[-1]
    return getattr(import_module(modul), class_name)