# -*- coding: utf-8 -*-
from django.db import models


class User(models.Model):
    user_code = models.CharField(max_length=200, verbose_name=u'编码')
    user_name = models.CharField(max_length=200, verbose_name=u'名称')

    def __unicode__(self):
        return unicode(self.user_name)


class Account(models.Model):

    """docstring for Account"""
    user = models.ForeignKey(User)
    LOGIN_TYPE = (
        ('0', 'Form'),
        ('1', 'FingerPrint'),
    )
    logintype = models.CharField(
        max_length=1, choices=LOGIN_TYPE, verbose_name=u'类型')
    code = models.CharField(max_length=200, verbose_name=u'帐号')
    password = models.CharField(max_length=20, verbose_name=u'密码')
    fingerprint = models.ImageField(blank=True, verbose_name=u'指纹')

    def __unicode__(self):
        return unicode(self.code)
