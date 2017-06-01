# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def validate(self,request):
        errors = []
        if len(request.POST['name']) < 3:
            errors.append('First name must be more than three letters long.')
        if len(request.POST['username']) < 3:
            errors.append('Last name must be more than three letters long.')
        if len(request.POST['password']) < 8:
            errors.append('Password must be at least 8 charachters.')
        if not request.POST['password'] == request.POST['confirm_pw']:
            errors.append('Password and confirmation password do not match')
        return errors
    # def item_validate(self,request):
    #     errors = []
    #     if len(request.POST['name']) == 0:
    #         errors.append('Item field cannot be empty!')
    #     if len(request.POST['name']) < 3:
    #         errors.append('Entry should be more than 3 characters.')
    #     return errors

class User(models.Model):
    name = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()


class Item(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()
