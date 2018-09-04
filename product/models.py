# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Banner(models.Model):
    imageUrl = models.CharField(max_length=200)
    path = models.CharField(max_length=200)
    description = models.CharField(max_length=100)
    def __unicode__(self):
        # 在Python3中使用 def __str__(self):
        return self.description
