# -*- coding:utf-8 -*-
import jieba
import os
import ConfigParser


def get_config(section, key):
    config = ConfigParser.ConfigParser()
    path = os.path.split(os.path.realpath(__file__))[0] + '/resource/win_settings.conf'
    config.read(path)
    return config.get(section, key)