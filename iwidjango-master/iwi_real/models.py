# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

'''
There needs to be a payment and a report structure

payment ref http://www.databaseanswers.org/data_models/payments_generic_model/index.htm

report can be seen as a flag system, so it can be treated on the application,
but that  is bound to lose some information, like who reported, what time, etc.
'''

class Profile(models.Model):
	id = models.AutoField(primary_key = True)
	
	# Profile info.
	age = models.IntegerField(default = 1, validators = [MaxValueValidator(150),
														 MinValueValidator(1)])

class Thread(models.Model):
	id = models.AutoField(primary_key = True)

	# Thread info.s
	title = models.CharField(default = "", max_length = 200)
	description = models.CharField(default = "", max_length = 1000)
	
	def __str__(self):
		return title

class Idea(models.Model):
	id = models.AutoField(primary_key = True)
	thread = models.ForeignKey(Thread, on_delete = models.CASCADE)
	
	# Idea info.
	title = models.CharField(default = "", max_length = 200)
	description = models.CharField(default = "", max_length = 1000)
	rate = models.IntegerField(default = 3, validators = [MaxValueValidator(5),
														 MinValueValidator(1)])

	def __str__(self):
		return title

class Tag(models.Model):
	id = models.AutoField(primary_key=True)
	idea = models.ForeignKey(Idea, on_delete = models.CASCADE)
	
	# Tag info.
	name = models.CharField(default = "", max_length = 200)

	def __str__(self):
		return name

class TB_UserIdea(models.Model):
	id = models.AutoField(primary_key = True)
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	idea = models.ForeignKey(Idea, on_delete = models.CASCADE)
	admin = models.IntegerField(default = 0)




