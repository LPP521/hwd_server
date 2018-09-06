# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    user_token = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    password = models.CharField(max_length=24)
    avatar_url = models.CharField(max_length=200, default='')
    nick_name = models.CharField(max_length=20)
    def __unicode__(self):
        # 在Python3中使用 def __str__(self):
        return self.nick_name